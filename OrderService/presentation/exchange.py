import pika
from retry import retry


class Exchange:
    def __init__(self) -> None:
        self.connection = self._get_connection()
        self.channel = self.connection.channel()

        # create order service exchange
        self.channel.exchange_declare(exchange='order', exchange_type='fanout')



    def publish(self, message: str) -> None:
        self.channel.basic_publish(exchange='order',
                                   routing_key='',
                                   body=message)
        print(f'[x] Sent {message}')

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def _get_connection(self):
        return pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq-host'))

    def __del__(self):
        self.connection.close()