from pydantic import BaseModel


class MerchantDTO(BaseModel):
    name: str
    ssn: str
    email: str
    phone_number: str
    allows_discount: bool