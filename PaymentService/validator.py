class Validator:
    def __init__(self, handler):
        self.handler = handler

    def validate(self, card) -> bool:
        return self.handler.handle(card)
