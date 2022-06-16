FROM rabbitmq:3.8.14-management-alpine
ADD ./enabled_plugins /etc/rabbitmq/
RUN chown rabbitmq:rabbitmq /etc/rabbitmq/enabled_plugins
ADD ./rabbitmq.conf /etc/rabbitmq/
RUN chown rabbitmq:rabbitmq /etc/rabbitmq/rabbitmq.conf
ADD ./certs /etc/rabbitmq/certs
RUN chown rabbitmq:rabbitmq /etc/rabbitmq/certs