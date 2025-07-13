from typing import List
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..import models,schema
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter(
    prefix= "/table",
    tags= ['Table']
)

@router.get("/",response_model=List[schema.TableOut])
def get_table(db: Session = Depends(get_db)):

    table = db.query(models.Crypto).all()
    
    return table

@router.get("/{id}", response_model=schema.TableOut)
def get_specific_table(id: str, db: Session = Depends(get_db)):
    coin = db.query(models.Crypto).filter(models.Crypto.id == id).first()
    
    if not coin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Coin: {id}, was not found in the database.")
    return coin
