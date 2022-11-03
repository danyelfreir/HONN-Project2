import pika
from retry import retry


class RabbitMQ:
    def __init__(self) -> None:
        self.connection = self._get_connection()
        self.channel = self.connection.channel()

        # connect to order service exchange
        self.channel.exchange_declare(exchange='order', exchange_type='fanout')
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange='order', queue=self.queue_name)
        # /

        # create my exchange
        self.channel.exchange_declare(
            exchange='payment', exchange_type='fanout')

    def publish(self, message: str) -> None:
        self.channel.basic_publish(exchange='payment',
                                   routing_key='',
                                   body=message)
        print(f'[x] Sent {message}')

    def consume(self, callback) -> None:
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=callback,
                                   auto_ack=True)
        print('[*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def _get_connection(self):
        return pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq-host'))

    def __del__(self):
        self.connection.close()

