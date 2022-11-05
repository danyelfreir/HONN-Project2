from Handlers.abstract_handler import AbstractHandler


class CVCHandler(AbstractHandler):

    def handle(self, card: str) -> str:
        cvc = str(card["cvc"])
        if cvc.isnumeric() and len(cvc) == 3:
            return super().handle(card)
        else:
            return False
