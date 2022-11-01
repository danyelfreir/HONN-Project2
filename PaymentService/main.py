from PaymentService.card_validator import CardValidator
from database import Database
from payment_service import PaymentService
from rabbitmq import RabbitMQ


def main():
    rabbitmq = RabbitMQ()
    database = Database()
    card_validator = CardValidator()
    payment_service = PaymentService(rabbitmq, database, card_validator)

    payment_service.start()


if __name__ == '__main__':
    main()
