import base64
import cv2
import io
import keras

import numpy as np
from PIL import Image
from retinaface.pre_trained_models import get_model as get_detector
import pika
import logging


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
        for annotation in faces:
            x_min, y_min, x_max, y_max = annotation["bbox"]

            x_min = int(np.clip(x_min, 0, x_max))
            y_min = int(np.clip(y_min, 0, y_max))

            crop = img[int(y_min):int(y_max), int(x_min):int(x_max)]
            crop = cv2.resize(crop, (128, 128))
            crop = np.reshape(crop, [1, 128, 128, 3]) / 255.0

            mask_result = self.model.predict(crop)
            has_mask = mask_result.argmax()

            cv2.putText(img, self._mask_label[has_mask], (x_min, y_min - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                        self._rect_label[has_mask], 2)
            cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), self._rect_label[has_mask], 1)

        return img

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
                 queue="default_queue"):
        super().__init__(path_to_model)
        logging.basicConfig(level=logging.INFO)
        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self.queue = queue
        self._channel.queue_declare(queue=self.queue)
        logging.info('App started waiting for messages...')

    def receive_msg(self):
        self._channel.basic_consume(
            queue=self.queue,
            on_message_callback=self._publish_msg,
            auto_ack=True
        )
        self._channel.start_consuming()

    def _publish_msg(self, ch, method, properties, body):
        data = body.decode("utf-8")
        logging.info("Data Received : {}".format(data))

    @staticmethod
    def _img_to_base64(img):
        base64_str = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
        return base64_str

    @staticmethod
    def _base64_to_img(base64_string):
        imgdata = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(imgdata))
        return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
