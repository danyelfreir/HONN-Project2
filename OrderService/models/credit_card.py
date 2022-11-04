from pydantic import BaseModel

class CreditCard(BaseModel):
    card_number: str
    expiration_month: int
    expiration_year: int
    cvc: int