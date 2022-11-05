import pika
from retry import retry


class RabbitMQ:
    def __init__(self) -> None:
        self.connection = self._get_connection()
        self.channel = self.connection.channel()

        # declare exhange
        # exchange should already be declared by services, this is a precaution
        self.channel.exchange_declare(exchange='order', exchange_type='fanout') # TODO should not be fanout
        self.channel.exchange_declare(exchange='payment', exchange_type='direct')

        # declare two queues, one for order and one for payment
        self.channel.queue_declare(queue='order-queue')
        self.channel.queue_declare(queue='payment-queue')

        # connect queues to respective exchanges
        self.channel.queue_bind(exchange='order', queue='order-queue')
        self.channel.queue_bind(exchange='payment', queue='payment-queue')


    def consume(self, order_callback, payment_callback) -> None:
        self.channel.basic_consume(queue='order-queue',
                                   on_message_callback=order_callback)
        self.channel.basic_consume(queue='payment-queue',
                                   on_message_callback=payment_callback)
        print('[*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def _get_connection(self):
        return pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq-host'))

    def __del__(self):
        self.connection.close()
