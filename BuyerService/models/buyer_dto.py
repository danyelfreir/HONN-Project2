from pydantic import BaseModel


class BuyerDTO(BaseModel):
    name: str
    ssn: str
    email: str
    phone_number: str