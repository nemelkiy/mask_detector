import pika
from RabbitMQConnection import RabbitMQConnectionHandler
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("pika").setLevel(logging.WARNING)

if __name__ == '__main__':
    rmq_credentials = pika.PlainCredentials('admin', 'Admin1234')
    rmq_parameters = pika.ConnectionParameters(host='rabbitmq-1', credentials=rmq_credentials, heartbeat=0, port=5672)
    rmq_handler = RabbitMQConnectionHandler(rmq_parameters)
    rmq_handler.listen_movie_requests()
