from .models import Crypto
from .database import SessionLocal


def insert_df_to_db(df):
    with SessionLocal() as session:
        for _, row in df.iterrows():
            coin = Crypto(**row.to_dict())
            session.merge(coin)
        session.commit()



