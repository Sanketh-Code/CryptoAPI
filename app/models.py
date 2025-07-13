from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String, Boolean, text
from .database import Base

class Crypto(Base):
    __tablename__ = "currency"

    id = Column(String, primary_key= True, nullable= False)
    symbol = Column(String, nullable=False)
    name = Column(String, nullable=False)
    current_price = Column(Float, nullable=False)
    market_cap = Column(Float, nullable=False)
    price_change_percentage_24h = Column(Float, nullable=False)
    ath = Column(Float, nullable=False)
    ath_date = Column(TIMESTAMP(timezone= True), nullable=False)
    last_updated = Column(TIMESTAMP(timezone= True), nullable=False)

class BTCPrices(Base):
    __tablename__ = "btc_prices"

    id = Column(Integer, primary_key=True, index=True)
    current_price = Column(Float, nullable=False)
    price_change_percentage_24h = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), default=datetime.utcnow, nullable=False)
