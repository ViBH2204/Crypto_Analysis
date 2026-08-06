import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# Crypto tickers on Yahoo Finance
tickers = {
    "BTC-USD": ("Bitcoin", "BTC"),
    "ETH-USD": ("Ethereum", "ETH"),
    "USDT-USD": ("Tether", "USDT"),
    "SOL-USD": ("Solana", "SOL"),
    "ADA-USD": ("Cardano", "ADA")
}

all_data = []

print("Fetching real historical data for all cryptocurrencies...")

for ticker, (name, symbol) in tickers.items():
    print(f"Downloading history for {name} ({symbol})...")
    # Fetch all-time daily historical data ('max' period)
    df_ticker = yf.download(ticker, period="max", interval="1d")
    
    df_ticker = df_ticker.reset_index()
    
    # Flatten multi-index columns if returned by newer yfinance versions
    if isinstance(df_ticker.columns, pd.MultiIndex):
        df_ticker.columns = [col[0] for col in df_ticker.columns]
        
    df_ticker["Coin_Name"] = name
    df_ticker["Symbol"] = symbol
    df_ticker["Price_USD"] = df_ticker["Close"].round(2)
    
    # Calculate 24h percentage change from previous day close
    df_ticker["Change_24h"] = (df_ticker["Close"].pct_change() * 100).round(2).fillna(0)
    
    # Use Volume as a proxy metric or set Market Cap column
    df_ticker["Market_Cap"] = df_ticker["Volume"].round(2)
    df_ticker["Timestamp"] = pd.to_datetime(df_ticker["Date"]).dt.strftime("%Y-%m-%d %H:%M:%S")
    
    # Filter to match our database schema
    df_clean = df_ticker[["Coin_Name", "Symbol", "Price_USD", "Change_24h", "Market_Cap", "Timestamp"]]
    all_data.append(df_clean)

# Combine datasets for all coins
final_df = pd.concat(all_data, ignore_index=True)

# Replace table in SQLite with real historical data
engine = create_engine("sqlite:///crypto_analytics.db")
final_df.to_sql("crypto_prices", engine, if_exists="replace", index=False)

print(f"\nDone! Overwrote database with {len(final_df)} rows of real historical market data.")