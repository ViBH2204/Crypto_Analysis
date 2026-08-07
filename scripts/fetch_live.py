from datetime import datetime
import requests
import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_PATH, COINS

engine = create_engine(f"sqlite:///{DATABASE_PATH}")

URL = (
    "https://api.coingecko.com/api/v3/coins/markets"
    "?vs_currency=usd"
    "&ids=bitcoin,ethereum,tether,solana,cardano"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

print("=" * 60)
print("FETCHING LIVE MARKET DATA")
print("=" * 60)

response = requests.get(URL, headers=HEADERS, timeout=30)
response.raise_for_status()

coins = response.json()

coin_lookup = {
    values[0]: coin_id
    for coin_id, values in COINS.items()
}

rows = []

snapshot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for coin in coins:

    rows.append({

        "Coin_ID":
            coin_lookup[coin["id"]],

        "Snapshot_Time":
            snapshot_time,

        "Current_Price":
            coin["current_price"],

        "Market_Cap":
            coin["market_cap"],

        "Volume_24h":
            coin["total_volume"],

        "Change_24h":
            coin["price_change_percentage_24h"],

        "Circulating_Supply":
            coin["circulating_supply"]

    })

df = pd.DataFrame(rows)

df.to_sql(
    "fact_live_metrics",
    engine,
    if_exists="append",
    index=False
)

print(df)

print()
print("=" * 60)
print(f"Inserted {len(df)} live records.")
print("=" * 60)