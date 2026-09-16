import requests

BASE = "https://api.elections.kalshi.com/trade-api/v2"

def list_open_markets(limit=50):
    resp = requests.get(f"{BASE}/markets", params={"status": "open", "limit": limit})
    resp.raise_for_status()
    return resp.json()["markets"]

def get_orderbook(ticker):
    resp = requests.get(f"{BASE}/markets/{ticker}/orderbook")
    resp.raise_for_status()
    return resp.json()