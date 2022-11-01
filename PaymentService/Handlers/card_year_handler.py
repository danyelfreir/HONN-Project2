from Handlers.abstract_handler import AbstractHandler


class YearHandler(AbstractHandler):

    def handle(self, request: str) -> str:
        year = request.card.year
        if request.isnumeric() and len(year) == 4:
            return super().handle(request)
        else:
            return False
