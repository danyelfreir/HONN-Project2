import string
from pydantic import BaseModel
from models.credit_card import CreditCard

class Order(BaseModel):
    product_id: int
    merchant_id: int
    buyer_id: int
    credit_card: CreditCard
    discount: float

class SavedOrder(BaseModel):
    product_id: int
    merchant_id: int
    buyer_id: int
    card_number: str
    total_price: float

class ForwardOrder(BaseModel):
    product_id: int
    merchant_id: int
    buyer_id: int
    buyer: dict
    credit_card: dict
    total_price: float


