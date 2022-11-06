from pydantic import BaseModel


class BuyerModel(BaseModel):
    buyer_id: str
    name: str
    ssn: str
    email: str
    phone_number: str