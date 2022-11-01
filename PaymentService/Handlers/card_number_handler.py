from Handlers.abstract_handler import AbstractHandler


class CardNumberHandler(AbstractHandler):
    # TODO: Implement the handle method
    def handle(self, request: str) -> str:
        if request.isnumeric() and len(request) == 16:
            return super().handle(request)
        else:
            return False
