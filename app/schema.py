from typing import Optional
from pydantic import BaseModel,EmailStr,conint
from datetime import datetime

class TableOut(BaseModel):
    id : str
    symbol : str
    current_price: float
    market_cap : float
    ath: float
    ath_date : datetime
    last_updated : datetime


    class Config:
        orm_mode = True

class BtcOut(BaseModel):
    id : int
    current_price: float
    price_change_percentage_24h: float
    timestamp: datetime

    