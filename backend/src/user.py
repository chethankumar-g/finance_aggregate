from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    password: str
    gender: str

class UserCreate(UserBase):
    transactions: List[float]
    amount: float

class User(UserBase):
    customer_id: int
    transactions: List[float]
    amount: float

    class Config:
        orm_mode = True