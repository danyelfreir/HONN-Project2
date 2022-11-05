from pydantic import BaseModel


class ProductModel(BaseModel):
    product_id: int
    merchant_id: int
    name: str
    price: float
    quantity: int
    reserved: int