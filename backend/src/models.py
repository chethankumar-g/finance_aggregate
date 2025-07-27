from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    step = Column(Integer, primary_key=True)
    customer_id = Column(String(10), ForeignKey('users.customer_id'))
    age = Column(Integer)
    gender = Column(String(10))
    zipcodeOri = Column(Integer)
    merchant_id = Column(Integer, ForeignKey('merchants.merchant_id'))
    zipMerchant = Column(Integer)
    category = Column(String(50))
    amount = Column(Float)
    fraud = Column(Integer)

    customer = relationship("User", back_populates="transactions")
    merchant = relationship("Merchant", back_populates="transactions")

class User(Base):
    __tablename__ = 'users'

    customer_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(128))  # Hashed password
    gender = Column(String(10))
    transactions = relationship("Transaction", back_populates="customer")

class Merchant(Base):
    __tablename__ = 'merchants'

    merchant_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('users.customer_id'))  # One merchant can have multiple customers
    name = Column(String(50))
    password = Column(String(128))  # Hashed password
    category = Column(String(50))
    transactions = relationship("Transaction", back_populates="merchant")