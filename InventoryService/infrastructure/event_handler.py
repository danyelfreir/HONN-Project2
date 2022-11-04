import json

from infrastructure.rabbitmq import RabbitMQ
from presentation.events import Events


class InventoryEventHandler:
    def __init__(self, events: Events):
        self.__rabbit = None
        self.__events = events

    def run(self):
        self.__rabbit = RabbitMQ()
        self.__rabbit.consume(self.__handle)

    def __handle(self, ch, method, properties, order) -> None:
        """Callback function for rabbitmq consume

        Args:
            ch (_type_): _description_
            method (_type_): _description_
            properties (_type_): _description_
            order (_type_): _description_
        """
        order_json = json.loads(order)
        product_id = int(order_json['product_id'])
        if method.routing_key == 'Payment-Successful':
            print(f" [x] Successful purchase")
            self.__events.sell_item(product_id)
        elif method.routing_key == 'Payment-Failure':
            print(f" [x] Unsuccessful purchase")
            self.__events.remove_reservation(product_id)
