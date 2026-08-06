import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# 1. Define the cryptocurrencies to track
COINS = "bitcoin,ethereum,tether,solana,cardano"
URL = f"https://api.coingecko.com/api/v3/simple/price?ids={COINS}&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"

def run_etl():
    print("Starting ETL pipeline...")
    
    # 2. Extract: Fetch data from CoinGecko API
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return
        
    data = response.json()
    
    # 3. Transform: Parse JSON into structured rows
    rows = []
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Symbol mapping dictionary
    symbols = {
        "bitcoin": "BTC",
        "ethereum": "ETH",
        "tether": "USDT",
        "solana": "SOL",
        "cardano": "ADA"
    }

    for coin_id, metrics in data.items():
        rows.append({
            "Coin_Name": coin_id.capitalize(),
            "Symbol": symbols.get(coin_id, coin_id.upper()),
            "Price_USD": metrics.get("usd"),
            "Change_24h": round(metrics.get("usd_24h_change", 0), 2),
            "Market_Cap": metrics.get("usd_market_cap"),
            "Timestamp": current_time
        })
        
    df = pd.DataFrame(rows)
    
    # 4. Load: Connect to SQLite and append rows
    engine = create_engine("sqlite:///crypto_analytics.db")
    
    # 'append' ensures existing historical data is preserved while new rows are added
    df.to_sql("crypto_prices", engine, if_exists="append", index=False)
    print(f"[{current_time}] Successfully logged {len(df)} records to SQLite database!")

if __name__ == "__main__":
    run_etl()