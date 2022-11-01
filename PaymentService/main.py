from Handlers.card_cvc_handler import CVCHandler
from Handlers.card_month_handler import MonthHandler
from Handlers.card_number_handler import CardNumberHandler
from Handlers.card_year_handler import YearHandler
from database import Database
from payment_service import PaymentService
from validator import Validator
from rabbitmq import RabbitMQ


def create_handler():
    number_handler = CardNumberHandler()
    month_handler = MonthHandler()
    year_handler = YearHandler()
    cvc_handler = CVCHandler()
    number_handler.set_next(month_handler).set_next(
        year_handler).set_next(cvc_handler)
    return number_handler


def main():
    rabbitmq = RabbitMQ()
    database = Database()
    handler = create_handler()
    validator = Validator(handler)
    payment_service = PaymentService(rabbitmq, database, validator)

    payment_service.start()


if __name__ == '__main__':
    main()
