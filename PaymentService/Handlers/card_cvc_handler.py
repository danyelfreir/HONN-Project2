from Handlers.abstract_handler import AbstractHandler


class CVCHandler(AbstractHandler):

    def handle(self, request: str) -> str:
        cvc = request.card.cvc
        if cvc.isnumeric() and len(cvc) == 3:
            return super().handle(request)
        else:
            return False
