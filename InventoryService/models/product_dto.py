from pydantic import BaseModel


class ProductDTO(BaseModel):
    merchant_id: int
    name: str
    price: float
    quantity: int
    reserved: int