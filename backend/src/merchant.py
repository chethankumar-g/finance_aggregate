from pydantic import BaseModel
from typing import List, Optional

class MerchantBase(BaseModel):
    name: str
    password: str
    category: str

class MerchantCreate(MerchantBase):
    customer_id: List[int]

class Merchant(MerchantBase):
    merchant_id: int
    customer_id: List[int]

    class Config:
        orm_mode = True