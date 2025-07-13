from fastapi import FastAPI
from .import models, database
from app.transform import load_df
from app.insert import insert_df_to_db
from .btc_tracking import save_btc_snapshot
from .routers import table, btc
from apscheduler.schedulers.background import BackgroundScheduler


app = FastAPI()
app.include_router(table.router)
app.include_router(btc.router)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(save_btc_snapshot, 'interval', minutes=2)  
    scheduler.start()

@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=database.engine)  
    start_scheduler()  


