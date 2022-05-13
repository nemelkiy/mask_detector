import pika
from RabbitMQConnection import RabbitMQConnectionHandler
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    rmq_parameters = pika.URLParameters('amqp://admin:Admin1234@rabbitmq-1:5672/%2F')
    rmq_handler = RabbitMQConnectionHandler(rmq_parameters)
    rmq_handler.listen_movie_requests()
