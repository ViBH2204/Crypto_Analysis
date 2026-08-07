import sqlite3
from config import DATABASE_PATH

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# ======================================================
# Latest Live Metrics View
# ======================================================

cursor.execute("""

DROP VIEW IF EXISTS vw_latest_live_metrics;

""")

cursor.execute("""

CREATE VIEW vw_latest_live_metrics AS

SELECT
    f.Coin_ID,
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
ON f.Coin_ID = d.Coin_ID

WHERE f.Snapshot_Time =

(
    SELECT MAX(Snapshot_Time)
    FROM fact_live_metrics
);

""")



cursor.execute("""

DROP VIEW IF EXISTS vw_price_history;

""")

cursor.execute("""

CREATE VIEW vw_price_history AS

SELECT

    p.Date,

    d.Coin_Name,

    d.Symbol,

    p.Open,
    p.High,
    p.Low,
    p.Close,
    p.Adj_Close,
    p.Volume

FROM fact_price_history p

JOIN dim_coin d

ON p.Coin_ID = d.Coin_ID;

""")


conn.commit()
conn.close()

print("=" * 50)
print("VIEW CREATED SUCCESSFULLY")
print("=" * 50)