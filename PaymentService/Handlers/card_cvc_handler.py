from Handlers.abstract_handler import AbstractHandler


class CVCHandler(AbstractHandler):

    def handle(self, request: str) -> str:
        if request.isnumeric() and len(request) == 3:
            return super().handle(request)
        else:
            return False
