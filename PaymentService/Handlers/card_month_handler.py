from Handlers.abstract_handler import AbstractHandler


class MonthHandler(AbstractHandler):

    def handle(self, card: int) -> str:
        month = str(card["expiration_month"])
        if month.isnumeric() and 1 <= int(month) <= 12:
            return super().handle(card)
        else:
            return False
