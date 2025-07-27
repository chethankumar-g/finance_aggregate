from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import models, db_config
import merchant as merchant_schema

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/merchants/", response_model=merchant_schema.Merchant)
def create_merchant(merchant: merchant_schema.MerchantCreate, db: Session = Depends(get_db)):
    db_merchant = models.Merchant(**merchant.dict())
    db.add(db_merchant)
    db.commit()
    db.refresh(db_merchant)
    return db_merchant

@router.get("/merchants/{merchant_id}", response_model=merchant_schema.Merchant)
def read_merchant(merchant_id: int, db: Session = Depends(get_db)):
    db_merchant = db.query(models.Merchant).filter(models.Merchant.id == merchant_id).first()
    if db_merchant is None:
        raise HTTPException(status_code=404, detail="Merchant not found")
    return db_merchant

@router.get("/merchants/", response_model=list[merchant_schema.Merchant])
def read_merchants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    merchants = db.query(models.Merchant).offset(skip).limit(limit).all()
    return merchants