import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from config import DATABASE_PATH, COINS

engine = create_engine(f"sqlite:///{DATABASE_PATH}")

print("=" * 60)
print("DOWNLOADING HISTORICAL DATA")
print("=" * 60)

all_rows = []

for coin_id, (cg_id, coin_name, symbol) in COINS.items():

    ticker = f"{symbol}-USD"

    print(f"Downloading {coin_name}...")

    df = yf.download(
        ticker,
        period="max",
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    if df.empty:
        print(f"❌ No data for {coin_name}")
        continue

    df = df.reset_index()

    # Fix newer yfinance versions
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]

    df = df.rename(columns={
        "Date": "Date",
        "Open": "Open",
        "High": "High",
        "Low": "Low",
        "Close": "Close",
        "Adj Close": "Adj_Close",
        "Volume": "Volume"
    })

    df["Coin_ID"] = coin_id

    df = df[
        [
            "Coin_ID",
            "Date",
            "Open",
            "High",
            "Low",
            "Close",
            "Adj_Close",
            "Volume",
        ]
    ]

    all_rows.append(df)

historical = pd.concat(all_rows, ignore_index=True)

historical.to_sql(
    "fact_price_history",
    engine,
    if_exists="replace",
    index=False
)

print()
print("=" * 60)
print(f"Inserted {len(historical):,} historical records.")
print("=" * 60)