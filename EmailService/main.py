import os
from dotenv import load_dotenv
from email_settings import EmailSettings
from email_client import EmailClient
from rabbit_mq import RabbitMQ
from email_service import EmailService


def main():
    print("Starting email service...")
    load_dotenv()

    settings = EmailSettings(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    email_client = EmailClient(settings)
    rabbitmq = RabbitMQ()

    email_service = EmailService(email_client, rabbitmq)
    email_service.start()


if __name__ == '__main__':
    main()
