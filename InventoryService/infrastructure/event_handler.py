import json
import threading

from infrastructure.rabbitmq import RabbitMQ
from presentation.events import Events


class InventoryEventHandler(threading.Thread):
    # def __init__(self, rabbit: RabbitMQ, events: Events):
    def __init__(self, events: Events):
        threading.Thread.__init__(self)
        # self.__rabbit = rabbit
        self.__events = events

    def run(self):
        self.__rabbit = RabbitMQ()
        self.__rabbit.consume(self.__handle)

    def __handle(self, ch, method, properties, payment) -> None:
        """Callback function for rabbitmq consume

        Args:
            ch (_type_): _description_
            method (_type_): _description_
            properties (_type_): _description_
            order (_type_): _description_
        """
        payment_json = json.loads(payment)
        product_id = int(payment_json['product_id'])
        if properties.headers['is_successful'] == True:
            print(f" [x] Successful purchase")
            self.__events.sell_item(product_id)
        else:
            print(f" [x] Unsuccessful purchase")
            self.__events.remove_reservation(product_id)

    def stop(self):
        self.__rabbit.close()
