from Handlers.abstract_handler import AbstractHandler


class MonthHandler(AbstractHandler):

    def handle(self, request: str) -> str:
        if request.isnumeric() and len(request) == 2:
            return super().handle(request)
        else:
            return False
