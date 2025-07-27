from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from db_config import get_db
from transaction import TransactionCreate, TransactionResponse
from auth import decode_access_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
        
    user = db.query(models.User).filter(models.User.customer_id == user_id).first()
    if user is None:
        raise credentials_exception
    return user

@router.post("/transactions/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_transaction = models.Transaction(**transaction.dict(), customer_id=current_user.customer_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def read_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id, models.Transaction.customer_id == current_user.customer_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/transactions/", response_model=List[TransactionResponse])
def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    transactions = db.query(models.Transaction).filter(models.Transaction.customer_id == current_user.customer_id).offset(skip).limit(limit).all()
    return transactions