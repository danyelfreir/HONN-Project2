from Handlers.abstract_handler import AbstractHandler


class CardNumberHandler(AbstractHandler):
    # TODO: Implement the handle method
    def handle(self, request: str) -> str:
        card_number = request.card.number
        if card_number.isnumeric() and self._is_valid(card_number):
            return super().handle(request)
        else:
            return False

    def _is_valid(self, card_number: str) -> bool:
        sum = 0
        parity = len(card_number) % 2

        for i in range(1, len(card_number) + 1):
            if i % 2 == parity:
                sum += int(card_number[i - 1])
            elif int(card_number[i]) > 4:
                sum += 2*int(card_number[i - 1]) - 9
            else:
                sum += 2*int(card_number[i - 1])
        return sum % 10 == 0
