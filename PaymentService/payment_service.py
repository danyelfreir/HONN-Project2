import json
from card_validator import CardValidator
from rabbitmq import RabbitMQ


class PaymentService:
    def __init__(self, rabbitmq: RabbitMQ, database, validator : CardValidator):
        self.rabbitmq = rabbitmq
        self.database = database
        self.card_validator = validator

    def start(self):
        """Starts consuming the order queue, passing in the callback function"""
        self.rabbitmq.consume(self._process_order)

    def _process_order(self, ch, method, properties, body):
        order = json.loads(body.decode())

        card_is_valid = self.card_validator.validate(order["credit_card"])
        self.database.insert(order['order_id'], card_is_valid)

        route = 'Payment-Successful' if card_is_valid else 'Payment-Failure'
        self.rabbitmq.publish(route, json.dumps(order))

        ch.basic_ack(delivery_tag=method.delivery_tag)
