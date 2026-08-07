import sqlite3
import pandas as pd

# CHANGE THIS TO YOUR DATABASE PATH
DB_PATH = r"C:\Users\ahluw\OneDrive\Desktop\CRYPTO ANALYSIS\database\crypto_analytics.db"

conn = sqlite3.connect(DB_PATH)

query = """
SELECT

d.Coin_ID,
d.Coin_Name,
d.Symbol,

f.Current_Price,
f.Market_Cap,
f.Volume_24h,
f.Change_24h,
f.Circulating_Supply,
f.Snapshot_Time

FROM fact_live_metrics f

JOIN dim_coin d
ON d.Coin_ID = f.Coin_ID

WHERE f.Snapshot_Time =
(
    SELECT MAX(Snapshot_Time)
    FROM fact_live_metrics
)

ORDER BY f.Market_Cap DESC
"""

dataset = pd.read_sql(query, conn)

conn.close()