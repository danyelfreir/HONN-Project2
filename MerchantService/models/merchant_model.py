from pydantic import BaseModel


class MerchantModel(BaseModel):
    merchant_id: int
    name: str
    ssn: str
    email: str
    phone_number: str
    allows_discount: bool
