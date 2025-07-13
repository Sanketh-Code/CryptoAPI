import time
import requests
import pandas as pd
from datetime import datetime
import logging
from .config import settings


base_url = f"{settings.base_url}"

def get_coin_info(coin):
    response = requests.get(f'{base_url}{coin}')
    if response.status_code == 200:
        return response.json()
    else:
        logging.warning(f"Failed to fetch data for {coin}. Status Code {response.status_code}")
        return None

    

def store_info(crypto):
    coin = get_coin_info(crypto)
    if coin is None:
        return None

    try:
        coin_info = {
            "id": coin["id"],
            "symbol": coin["symbol"],
            "name": coin["name"],
            "current_price": coin["market_data"]["current_price"]["usd"],
            "market_cap": coin["market_data"]["market_cap"]["usd"],
            "price_change_percentage_24h": coin["market_data"]["price_change_percentage_24h"],
            "ath": coin["market_data"]["ath"]["usd"],
            "ath_date": coin["market_data"]["ath_date"]["usd"],
            "last_updated": coin["last_updated"]
        }
        return coin_info

    except (KeyError, TypeError) as e:
        logging.warning(f"Skipping {crypto} due to error: {e}")
        return None


def load_df(crypto_list):
    df = pd.DataFrame()
    n = len(crypto_list)
    records = []
    for i in range(0,n):
        info = store_info(crypto_list[i])
        if info is not None:
            records.append(info)
        time.sleep(1)
    df = pd.DataFrame(records)
    df["ath_date"] = pd.to_datetime(df["ath_date"])
    df["last_updated"] = pd.to_datetime(df["last_updated"])
    return df