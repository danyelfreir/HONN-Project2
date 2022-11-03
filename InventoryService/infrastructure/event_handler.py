from infrastructure.rabbitmq import RabbitMQ


class InventoryEventHandler:
    def __init__(self, rabbit: RabbitMQ):
        self.__rabbit = rabbit

    def start(self):
        self.__rabbit.consume()
