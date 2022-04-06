from buisness_logic import Recognizer
import pika


def main():
    params = pika.URLParameters('amqp://admin:Admin1234@rabbitmq-1:5672/%2F')
    rec = Recognizer(path_to_model="/app/model/my_model.h5",
                     params=params,
                     queue="default_queue",
                     queue_pub="default_queue_pub")
    rec.receive_msg()


if __name__ == '__main__':
    main()
