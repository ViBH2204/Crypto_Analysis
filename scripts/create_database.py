import sqlite3
from config import DATABASE_PATH, COINS

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# ======================================================
# DIMENSION TABLE
# ======================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_coin (

    Coin_ID INTEGER PRIMARY KEY,

    CoinGecko_ID TEXT NOT NULL UNIQUE,

    Coin_Name TEXT NOT NULL,

    Symbol TEXT NOT NULL

)
""")

# ======================================================
# FACT TABLE
# Historical Prices
# ======================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS fact_price_history (

    Price_ID INTEGER PRIMARY KEY AUTOINCREMENT,

    Coin_ID INTEGER,

    Date DATE,

    Open REAL,

    High REAL,

    Low REAL,

    Close REAL,

    Adj_Close REAL,

    Volume REAL,

    FOREIGN KEY (Coin_ID)
        REFERENCES dim_coin(Coin_ID)

)

""")

# ======================================================
# FACT TABLE
# Live Metrics
# ======================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS fact_live_metrics (

    Snapshot_ID INTEGER PRIMARY KEY AUTOINCREMENT,

    Coin_ID INTEGER,

    Snapshot_Time TEXT,

    Current_Price REAL,

    Market_Cap REAL,

    Volume_24h REAL,

    Change_24h REAL,

    Circulating_Supply REAL,

    FOREIGN KEY (Coin_ID)
        REFERENCES dim_coin(Coin_ID)

)

""")

# ======================================================
# INSERT COINS
# ======================================================

cursor.execute("DELETE FROM dim_coin")

for coin_id, values in COINS.items():

    cg_id, name, symbol = values

    cursor.execute("""

    INSERT INTO dim_coin

    VALUES (?, ?, ?, ?)

    """, (coin_id, cg_id, name, symbol))

conn.commit()
conn.close()

print("="*50)
print("DATABASE CREATED SUCCESSFULLY")
print("="*50)