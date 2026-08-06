from datetime import datetime
import pandas as pd
import requests
from sqlalchemy import create_engine

# 1. Define the cryptocurrencies to track
COINS = "bitcoin,ethereum,tether,solana,cardano"
URL = f"https://api.coingecko.com/api/v3/simple/price?ids={COINS}&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"

# Custom headers to bypass Cloudflare bot detection on GitHub Actions
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
}


def run_etl():
  print("Starting ETL pipeline...")

  # 2. Extract: Fetch data from CoinGecko API with a 10-second timeout
  try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()  # Raises an exception for 4xx/5xx errors
  except requests.exceptions.RequestException as e:
    print(f"Failed to fetch data from CoinGecko: {e}")
    raise e  # Fail the GitHub Actions job explicitly so you get notified

  data = response.json()

  # 3. Transform: Parse JSON into structured rows
  rows = []
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  symbols = {
      "bitcoin": "BTC",
      "ethereum": "ETH",
      "tether": "USDT",
      "solana": "SOL",
      "cardano": "ADA",
  }

  for coin_id, metrics in data.items():
    rows.append({
        "Coin_Name": coin_id.capitalize(),
        "Symbol": symbols.get(coin_id, coin_id.upper()),
        "Price_USD": metrics.get("usd"),
        "Change_24h": round(metrics.get("usd_24h_change", 0), 2),
        "Market_Cap": metrics.get("usd_market_cap"),
        "Timestamp": current_time,
    })

  df = pd.DataFrame(rows)

  # 4. Load: Connect to SQLite and append rows
  engine = create_engine("sqlite:///crypto_analytics.db")
  df.to_sql("crypto_prices", engine, if_exists="append", index=False)

  print(
      f"[{current_time}] Successfully logged {len(df)} records to SQLite"
      " database!"
  )


if __name__ == "__main__":
  run_etl()