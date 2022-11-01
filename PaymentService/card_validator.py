from Handlers.card_cvc_handler import CVCHandler
from Handlers.card_month_handler import MonthHandler
from Handlers.card_number_handler import CardNumberHandler
from Handlers.card_year_handler import YearHandler
from Handlers.i_handler import IHandler


class CardValidator:
    def __init__(self):
        self.handler = self._create_chain()

    def _create_chain(self) -> IHandler:
        number_handler = CardNumberHandler()
        month_handler = MonthHandler()
        year_handler = YearHandler()
        cvc_handler = CVCHandler()
        number_handler.set_next(month_handler).set_next(
            year_handler).set_next(cvc_handler)
        return number_handler

    def validate(self, card) -> bool:
        return self.handler.handle(card)
