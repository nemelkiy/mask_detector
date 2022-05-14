from buisness_logic import Recognizer
import pika


def main():
    params = pika.URLParameters('amqp://admin:Admin1234@rabbitmq-1:5672/%2F')
    rec = Recognizer(path_to_model="/app/model/my_model.h5",
                     params=params,
                     queue="shots_for_processing",
                     queue_pub="result_shots")
    rec.receive_msg()


if __name__ == '__main__':
    main()
