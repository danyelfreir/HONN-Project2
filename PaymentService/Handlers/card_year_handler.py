from Handlers.abstract_handler import AbstractHandler


class YearHandler(AbstractHandler):

    def handle(self, card: str) -> str:
        year = str(card["expiration_year"])
        if year.isnumeric() and len(year) == 4:
            return super().handle(card)
        else:
            return False
