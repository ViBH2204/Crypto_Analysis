import pandas as pd
from sqlalchemy import create_engine

# Connect to the SQLite database
engine = create_engine("sqlite:///crypto_analytics.db")

print("\n==========================================================")
print("--- QUERY 1: 30-DAY SUMMARY METRICS PER COIN ---")
print("==========================================================")

q1 = """
WITH RankedPrices AS (
    SELECT 
        Coin_Name, 
        Symbol, 
        Price_USD, 
        Change_24h,
        Timestamp,
        FIRST_VALUE(Price_USD) OVER (PARTITION BY Symbol ORDER BY Timestamp DESC) AS Current_Price
    FROM crypto_prices
    WHERE Timestamp >= date((SELECT MAX(Timestamp) FROM crypto_prices), '-30 days')
)
SELECT 
    Coin_Name, 
    Symbol, 
    Current_Price,
    ROUND(AVG(Price_USD), 2) AS Avg_Price_30D,
    ROUND(MAX(Price_USD), 2) AS Peak_Price_30D,
    ROUND(MIN(Price_USD), 2) AS Lowest_Price_30D,
    ROUND(MAX(Change_24h), 2) AS Max_Single_Day_Gain_Pct
FROM RankedPrices
GROUP BY Coin_Name, Symbol, Current_Price
ORDER BY Current_Price DESC;
"""
df_q1 = pd.read_sql(q1, engine)
print(df_q1.to_string(index=False))


print("\n==========================================================")
print("--- TIMEFRAME COMPARISONS (1D, 1W, 1M, 1Y, 5Y, MAX) ---")
print("==========================================================")

# Timeframe modifiers for SQLite date functions
timeframes = {
    "1 Day (1D) Performance": "'-1 days'",
    "1 Week (1W) Performance": "'-7 days'",
    "1 Month (1M) Performance": "'-1 months'",
    "1 Year (1Y) Performance": "'-1 years'",
    "5 Year (5Y) Performance": "'-5 years'",
    "Max (All-Time) Performance": None  # None indicates all available historical data
}

for label, modifier in timeframes.items():
    if modifier:
        where_clause = f"WHERE Timestamp >= date((SELECT MAX(Timestamp) FROM crypto_prices), {modifier})"
    else:
        where_clause = ""  # For MAX, search all rows without date restrictions

    query = f"""
    WITH LatestPrices AS (
        -- Select the single most recent price for each coin
        SELECT Symbol, Coin_Name, Price_USD AS Current_Price
        FROM (
            SELECT Symbol, Coin_Name, Price_USD,
                   ROW_NUMBER() OVER (PARTITION BY Symbol ORDER BY Timestamp DESC) as rn
            FROM crypto_prices
        ) WHERE rn = 1
    ),
    StartPrices AS (
        -- Select the earliest recorded price within the specified time window
        SELECT Symbol, Price_USD AS Price_At_That_Time, Timestamp AS Start_Timestamp
        FROM (
            SELECT Symbol, Price_USD, Timestamp,
                   ROW_NUMBER() OVER (PARTITION BY Symbol ORDER BY Timestamp ASC) as rn
            FROM crypto_prices
            {where_clause}
        ) WHERE rn = 1
    )
    SELECT 
        l.Coin_Name,
        l.Symbol,
        l.Current_Price,
        s.Price_At_That_Time,
        s.Start_Timestamp AS Price_Date,
        ROUND(((l.Current_Price - s.Price_At_That_Time) / s.Price_At_That_Time) * 100, 2) AS Pct_Difference
    FROM LatestPrices l
    JOIN StartPrices s ON l.Symbol = s.Symbol
    ORDER BY l.Current_Price DESC;
    """
    
    df_result = pd.read_sql(query, engine)
    print(f"\n--- {label} ---")
    print(df_result.to_string(index=False))