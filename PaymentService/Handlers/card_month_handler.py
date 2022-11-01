from Handlers.abstract_handler import AbstractHandler


class MonthHandler(AbstractHandler):

    def handle(self, request: str) -> str:
        month = request.card.month
        if month.isnumeric() and 1 <= int(month) <= 12:
            return super().handle(request)
        else:
            return False
