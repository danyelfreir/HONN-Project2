import json


class PaymentService:
    def __init__(self, rabbitmq, database, validator):
        self.rabbitmq = rabbitmq
        self.database = database
        self.validator = validator

    def start(self):
        """Starts consuming the order queue, passing in the callback function"""
        self.rabbitmq.consume(self._process_order)

    def _process_order(self, ch, method, properties, order):
        """Callback function for rabbitmq consume

        Args:
            ch (_type_): _description_
            method (_type_): _description_
            properties (_type_): _description_
            order (_type_): _description_
        """
        # order = json.loads(order)
        print(f" [x] Received {order.decode()}")
        # is_valid = self.validator.validate(order)
        # self.database.insert(order.id, is_valid)
        # self.rabbitmq.publish(is_valid)
        res = order.decode() + "and processed by payment service"
        self.rabbitmq.publish(res)
