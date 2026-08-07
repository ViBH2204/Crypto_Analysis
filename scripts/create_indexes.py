import sqlite3
from config import DATABASE_PATH

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# ======================================================
# FACT PRICE HISTORY
# ======================================================

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_price_coin
ON fact_price_history(Coin_ID);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_price_date
ON fact_price_history(Date);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_price_coin_date
ON fact_price_history(Coin_ID, Date);
""")

# ======================================================
# FACT LIVE METRICS
# ======================================================

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_live_coin
ON fact_live_metrics(Coin_ID);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_live_snapshot
ON fact_live_metrics(Snapshot_Time);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_live_coin_snapshot
ON fact_live_metrics(Coin_ID, Snapshot_Time);
""")

conn.commit()
conn.close()

print("=" * 50)
print("INDEXES CREATED SUCCESSFULLY")
print("=" * 50)