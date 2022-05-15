import json
import logging
from json import JSONDecodeError

import pika

import VideoHandler

logging.basicConfig(level=logging.INFO)
logging.getLogger("pika").setLevel(logging.WARNING)


def callback(ch, method, properties, body):
    data = None
    try:
        data = json.loads(body)
    except JSONDecodeError as e:
        logging.error(f"Запрос невозможно конвертировать в JSON. Тело неудачного запроса: {body}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return
    if not data or not ('link' and 'fps' in data):
        logging.error(f"В запросе отсутствуют обязательные поля link и fps. Тело неудачного запроса: {data}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return
    logging.info(f"Получена ссылка на видео: {data['link']}. Частота кадров: {data['fps']}. Начало обработки.")
    logging.info("Видео загружается на диск.")
    video_path, video_title = VideoHandler.Downloader.download_movie(data['link'])
    if not video_path:
        logging.error(f"Ссылка на видеоисточник некорректна!Тело неудачного запроса: {data}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return
    logging.info("Видео успешно загружено. Запуск процедуры деления на кадры и отправки в RabbitMQ.")
    VideoHandler.VideoCutter.cut_movie_and_send_rmq(video_path,video_title, data['fps'], data['link'])
    logging.info(f"Конец обработки видео {video_title}. Ссылка: {data['link']}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


class RabbitMQConnectionHandler:
    def __init__(self, rmq_parameters):
        self.rmq_connection = pika.BlockingConnection(rmq_parameters)
        self.rmq_channel = self.rmq_connection.channel()

    def publish_shot(self, shot_path, link, movie_title, frame_number, frame_duration):
        self.rmq_channel.queue_declare(queue='shots_for_processing')
        json_body = VideoHandler.ShotHandler.convert_img_to_json(shot_path, link, movie_title, frame_number, frame_duration)
        self.rmq_channel.basic_publish(exchange='', routing_key='shots_for_processing', body=json_body)

    def listen_movie_requests(self):
        self.rmq_channel.queue_declare(queue='movie_requests')
        self.rmq_channel.basic_consume(queue='movie_requests', on_message_callback=callback, auto_ack=False)
        self.rmq_channel.start_consuming()
