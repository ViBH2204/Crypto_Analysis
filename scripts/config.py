from pathlib import Path

# Project Root
ROOT_DIR = Path(__file__).resolve().parent.parent

# Database Path
DATABASE_PATH = ROOT_DIR / "database" / "crypto_analytics.db"

# Cryptocurrencies
COINS = {
    1: ("bitcoin", "Bitcoin", "BTC"),
    2: ("ethereum", "Ethereum", "ETH"),
    3: ("tether", "Tether", "USDT"),
    4: ("solana", "Solana", "SOL"),
    5: ("cardano", "Cardano", "ADA")
}