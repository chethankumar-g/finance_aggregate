from pydantic import BaseModel
from typing import Optional

class TransactionBase(BaseModel):
    step: int
    customer_id: int
    age: int
    gender: str
    zipcodeOri: int
    merchant_id: int
    zipMerchant: int
    category: str
    amount: float
    fraud: bool

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int  # Assuming there's an ID for the transaction

    class Config:
        orm_mode = True

class TransactionResponse(TransactionBase):
    id: int
    customer_id: int
    fraud: bool = False

    class Config:
        orm_mode = True