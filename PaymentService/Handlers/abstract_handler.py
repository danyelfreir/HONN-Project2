from Handlers.i_handler import IHandler


class AbstractHandler(IHandler):

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: IHandler) -> IHandler:
        if self._next_handler is None:
            self._next_handler = handler
        else:
            self._next_handler.set_next(handler)
        return handler

    def handle(self, request: str) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return True
