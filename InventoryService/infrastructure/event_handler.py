import json
import threading

from infrastructure.rabbitmq import RabbitMQ
from presentation.events import Events


class InventoryEventHandler(threading.Thread):
    def __init__(self, rabbit: RabbitMQ, events: Events):
        print('inside init')
        threading.Thread.__init__(self)
        self.__rabbit = rabbit
        self.__events = events

    def run(self):
        print("HERE")
        self.__rabbit.consume(self.__handle)

    def __handle(self, ch, method, properties, payment) -> None:
        """Callback function for rabbitmq consume

        Args:
            ch (_type_): _description_
            method (_type_): _description_
            properties (_type_): _description_
            order (_type_): _description_
        """
        # payment_json = json.loads(payment)
        payment_json = int(payment)
        print(properties.headers['is_successful'])
        if properties.headers['is_successful'] == 'true':
            print(f" [x] Successful purchase")
            self.__events.sell_item(payment_json)
        else:
            print(f" [x] Unsuccessful purchase")
            self.__events.remove_reservation(payment_json)
