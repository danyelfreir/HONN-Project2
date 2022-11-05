from pydantic import BaseModel


class ProductModel(BaseModel):
    merchant_id: int
    product_name: str
    price: float
    quantity: int
    reserved: int