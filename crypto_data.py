# crypto_data.py
# Cryptocurrency database with sample data

crypto_db = {
    "Bitcoin": {
        "symbol": "BTC",
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3,
        "max_sustainability": 10,
        "description": "The original cryptocurrency with the largest market cap",
        "risk_level": "medium"
    },
    "Ethereum": {
        "symbol": "ETH",
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6,
        "max_sustainability": 10,
        "description": "Smart contract platform with strong developer ecosystem",
        "risk_level": "medium"
    },
    "Cardano": {
        "symbol": "ADA",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8,
        "max_sustainability": 10,
        "description": "Proof-of-stake blockchain focused on sustainability",
        "risk_level": "medium-high"
    },
    "Solana": {
        "symbol": "SOL",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "max_sustainability": 10,
        "description": "High-speed blockchain for decentralized applications",
        "risk_level": "high"
    },
    "Polygon": {
        "symbol": "MATIC",
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 9,
        "max_sustainability": 10,
        "description": "Ethereum scaling solution with low energy consumption",
        "risk_level": "medium-high"
    }
}

# Helper functions for data analysis
def get_most_sustainable():
    """Return the most sustainable cryptocurrency"""
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

def get_trending_cryptos():
    """Return cryptocurrencies with rising price trends"""
    return [crypto for crypto in crypto_db if crypto_db[crypto]["price_trend"] == "rising"]

def get_low_energy_cryptos():
    """Return cryptocurrencies with low energy usage"""
    return [crypto for crypto in crypto_db if crypto_db[crypto]["energy_use"] == "low"]

def get_high_market_cap_cryptos():
    """Return cryptocurrencies with high market cap"""
    return [crypto for crypto in crypto_db if crypto_db[crypto]["market_cap"] == "high"]