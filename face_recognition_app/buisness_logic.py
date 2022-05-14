import base64
import cv2
import io
import keras

import numpy as np
from PIL import Image
from retinaface.pre_trained_models import get_model as get_detector
import pika
import logging
import json


class RecognizerCore:
    _mask_label = {
        0: 'MASK',
        1: 'NO MASK'
    }

    _rect_label = {
        0: (0, 250, 0),  # green
        1: (250, 0, 0)  # red
    }

    def __init__(self, path_to_model: str):
        self.model = keras.models.load_model(path_to_model)

    def define_mask(self, img):
        faces = self._recognize_faces(img)
        masks = []
        for annotation in faces:
            x_min, y_min, x_max, y_max = annotation["bbox"]

            x_min = int(np.clip(x_min, 0, x_max))
            y_min = int(np.clip(y_min, 0, y_max))

            crop = img[int(y_min):int(y_max), int(x_min):int(x_max)]
            crop = cv2.resize(crop, (128, 128))
            crop = np.reshape(crop, [1, 128, 128, 3]) / 255.0

            mask_result = self.model.predict(crop)
            has_mask = mask_result.argmax()
            masks.append(has_mask)

            cv2.putText(img, self._mask_label[has_mask], (x_min, y_min - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                        self._rect_label[has_mask], 2)
            cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), self._rect_label[has_mask], 1)
        if 1 in masks:
            return img
        else:
            return False

    @staticmethod
    def _recognize_faces(img):
        face_detector = get_detector("resnet50_2020-07-20", max_size=800)
        face_detector.eval()
        faces = face_detector.predict_jsons(img)
        return faces


class Recognizer(RecognizerCore):

    def __init__(self,
                 path_to_model: str,
                 params=pika.URLParameters('amqp://rabbitmq:rabbitmq@rabbit1:5672/%2F'),
                 queue="default_queue",
                 queue_pub="default_queue_pub"):
        super().__init__(path_to_model)
        logging.basicConfig(level=logging.INFO)
        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self._channel_pub = self._connection.channel()
        self.queue = queue
        self.queue_pub = queue_pub
        self._channel.queue_declare(queue=self.queue)
        self._channel_pub.queue_declare(queue=self.queue_pub)
        logging.info('Приложение ожидает сообщений...')

    def receive_msg(self):
        self._channel.basic_consume(
            queue=self.queue,
            on_message_callback=self._publish_msg,
            auto_ack=False
        )
        self._channel.start_consuming()

    def _process_msg(self, data_json):
        img = self._base64_to_img(data_json["data"])
        result_img = self.define_mask(img)
        if type(result_img) != bool:
            img_base64 = self._img_to_base64(result_img)
            if img_base64:
                logging.info("Кадр обработан.")
            return img_base64
        else:
            logging.info("Кадр не удалось обработать.")
            return False

    def _publish_msg(self, ch, method, properties, body):
        data = body.decode("utf-8")
        logging.info(f"Данные получены.")
        data_json = json.loads(data)
        result = self._process_msg(data_json)
        if result:
            msg = self._post_process_data(data_json, result)
            self._channel_pub.basic_publish(exchange='',
                                        routing_key=self.queue_pub,
                                        body=str(msg))
            ch.basic_ack(delivery_tag=method.delivery_tag)
            logging.info(f"Данные отправлены. {str(msg)}")
        else:
            logging.info(f"Даннные не отправлены, но сообщение обработано")
            ch.basic_ack(delivery_tag=method.delivery_tag)

    @staticmethod
    def _post_process_data(data_json, img_base64: str):
        msg = {
            "link": data_json["link"],
            "title": data_json["title"],
            "shot_number": data_json["shot_number"],
            "frame_duration": data_json["frame_duration"],
            "data": img_base64
        }
        return msg

    @staticmethod
    def _img_to_base64(img):
        base64_str = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
        return base64_str

    @staticmethod
    def _base64_to_img(base64_string):
        imgdata = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(imgdata))
        return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
