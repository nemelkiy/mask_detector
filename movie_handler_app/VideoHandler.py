import base64
import json
import logging
import os
import shutil
from datetime import timedelta

import numpy as np
import pika
from pytube.exceptions import RegexMatchError

import RabbitMQConnection
from moviepy.editor import VideoFileClip
from pytube import YouTube

logging.basicConfig(level=logging.INFO)


class Downloader:
    @staticmethod
    def download_movie(link: str):
        path = "resources/video"
        try:
            yt = YouTube(link)
        except RegexMatchError as e:
            return None
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
        return f"{path}/{yt.title}.mp4"


class VideoCutter:
    @staticmethod
    def cut_movie_and_send_rmq(movie_path: str, fps: float, link: str):
        rmq_parameters = pika.URLParameters('amqp://admin:Admin1234@rabbitmq-1:5672/%2F')
        rmq_handler = RabbitMQConnection.RabbitMQConnectionHandler(rmq_parameters)
        video_clip = VideoFileClip(movie_path)
        movie_title = os.path.basename(os.path.normpath(movie_path))
        shots_dir = f"./resources/frames/{movie_title}"
        if not os.path.isdir(shots_dir):
            os.mkdir(shots_dir)
        saving_frames_per_second = min(video_clip.fps, fps)
        step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
        counter = 0
        for current_duration in np.arange(0, video_clip.duration, step):
            frame_duration_formatted = VideoCutter.format_timedelta(timedelta(seconds=current_duration)).replace(":",
                                                                                                                 "-")
            counter += 1
            shot_path = os.path.join(shots_dir, f"frame{frame_duration_formatted}.jpg")
            video_clip.save_frame(shot_path, current_duration)
            rmq_handler.publish_shot(shot_path, link, movie_title, counter, frame_duration_formatted)
        rmq_handler.rmq_connection.close()
        VideoCutter.clean(movie_path, shots_dir)

    @staticmethod
    def format_timedelta(td):
        result = str(td)
        try:
            result, ms = result.split(".")
        except ValueError:
            return result + ".00".replace(":", "-")
        ms = int(ms)
        ms = round(ms / 1e4)
        return f"{result}.{ms:02}".replace(":", "-")

    @staticmethod
    def clean(movie_path: str, shots_dir: str):
        os.remove(movie_path)
        shutil.rmtree(shots_dir)


class ShotHandler:
    @staticmethod
    def convert_img_to_json(path, link, movie_title, shot_number, frame_duration):
        data = ShotHandler.img_to_base64(path)
        preform = {"link": link,
                   "title": movie_title,
                   "shot_number": shot_number,
                   "frame_duration": frame_duration,
                   "data": data.decode("utf-8")}
        json_body = json.dumps(preform, ensure_ascii=False)
        return json_body

    @staticmethod
    def img_to_base64(img):
        with open(img, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string

