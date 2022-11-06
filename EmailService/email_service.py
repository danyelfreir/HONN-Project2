import json

class EmailService:
    def __init__(self, email_client, rabbitmq):
        self.email_client = email_client
        self.rabbitmq = rabbitmq

    def _order(self, ch, method, properties, body):
        order = json.loads(body.decode())
        email = order["buyer"].get("email")
        
        message = ["Summary", "-"*15,
                    f"Order id: {order['order_id']}",
                    f"Items: {order['inventory'].get('product_name')}",
                    f"Total: ${order['total_price']}"]
        self._send_email(email, "Order has been created", message)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def _payment(self, ch, method, properties, body):
        order = json.loads(body.decode())
        email = order["buyer"].get("email")
        if method.routing_key == 'Payment-Successful':
            self._send_email(email, "Order has been purchased", f"Order {order['order_id']} has been successfully purchased")
        elif method.routing_key == 'Payment-Failure':
            self._send_email(email, "Order purchase failed", f"Order {order['order_id']} purchase has failed.")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def _send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)

    def start(self):
        print("[X] Starting email service")
        self.rabbitmq.consume(self._order, self._payment)