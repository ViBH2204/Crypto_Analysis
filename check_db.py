import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///crypto_analytics.db")

# Read back table entries
df = pd.read_sql("SELECT * FROM crypto_prices", engine)
print("Database Contents:")
print(df)