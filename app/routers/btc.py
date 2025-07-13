from typing import List
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.responses import StreamingResponse
from ..import models,schema
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..utils import create_plot

router = APIRouter(
    prefix= "/btc",
    tags= ['Bitcoin']
)


@router.get("/",response_model= List[schema.BtcOut])
def get_btc_prices(db: Session = Depends(get_db)):
    table = db.query(models.BTCPrices).all()
    return table


@router.get("/graph/{column}")
def generate_graph(column: str ,db : Session = Depends(get_db)):

    valid_columns = [col.name for col in models.BTCPrices.__table__.columns]
    if column not in valid_columns:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The column name entered: {column} is not available"
        )
    selected_column = getattr(models.BTCPrices, column)
    results = db.query(models.BTCPrices.timestamp, selected_column).all()

    x_data = [row[0] for row in results]  # timestamps
    y_data = [row[1] for row in results]  # column values

    buf = create_plot(x_data, y_data, f"Flow of {column}", "Time", column)
    return StreamingResponse(buf, media_type="image/png")



