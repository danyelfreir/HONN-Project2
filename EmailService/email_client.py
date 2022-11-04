import yagmail

class EmailClient:
    def __init__(self, email_settings):
        self.email_settings = email_settings
        self.connection = yagmail.SMTP(self.email_settings.username(), self.email_settings.password())

    def send_email(self, recipient, subject, body):
        self.connection.send(recipient, subject, body)

    def __del__(self):
        self.connection.close()