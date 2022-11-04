class EmailService:
    def __init__(self, email_client, rabbitmq):
        self.email_client = email_client
        self.rabbitmq = rabbitmq

    def order(self, ch, method, properties, body):
        print(f'Received order {body.decode()}')
        # self.send_email(body.decode())

    def payment(self, ch, method, properties, body):
        print(f"Received payment {body.decode()}")
        # self.send_email(body.decode())

    def send_email(self, email):
        print("Sending email")
        self.email_client.send_email('patrekur20@ru.is', "To whom it may concern", email)

    def start(self):
        print("[X] Starting email service")
        self.rabbitmq.consume(self.order, self.payment)