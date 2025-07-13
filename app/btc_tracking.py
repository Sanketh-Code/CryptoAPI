from .models import BTCPrices
from .database import SessionLocal
from .transform import store_info
from datetime import datetime
import logging

def save_btc_snapshot():

    info = store_info("bitcoin")
    if info is None:
        logging.warning(f"Failed to fetch Bitcoin Data")
        return
    
    snapshot = BTCPrices(
        current_price=info["current_price"],
        price_change_percentage_24h=info["price_change_percentage_24h"],
        timestamp=datetime.utcnow()  
    )

    with SessionLocal() as session:
        session.add(snapshot)
        session.commit()

