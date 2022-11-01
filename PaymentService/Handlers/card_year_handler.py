from Handlers.abstract_handler import AbstractHandler


class YearHandler(AbstractHandler):

    def handle(self, request: str) -> str:
        if request.isnumeric() and len(request) == 4:
            return super().handle(request)
        else:
            return False
