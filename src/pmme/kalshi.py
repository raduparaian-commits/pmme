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

def list_markets_by_series(series_ticker, limit=50):
    resp = requests.get(
        f"{BASE}/markets",
        params={"status": "open", "series_ticker": series_ticker, "limit": limit},
    )
    resp.raise_for_status()
    return resp.json()["markets"]

def derive_ask_levels(ticker):
    raw = get_orderbook(ticker)
    book = raw["orderbook_fp"]

    yes_bids = sorted(
        [(float(p), float(s)) for p, s in (book.get("yes_dollars") or [])],
        key=lambda x: x[0], reverse=True  # highest bid first
    )
    no_bids = sorted(
        [(float(p), float(s)) for p, s in (book.get("no_dollars") or [])],
        key=lambda x: x[0], reverse=True
    )

    # highest NO bid -> cheapest YES ask, and order is preserved (now ascending)
    yes_asks = [(round(1.0 - p, 4), s) for p, s in no_bids]
    no_asks = [(round(1.0 - p, 4), s) for p, s in yes_bids]

    return {"yes_asks": yes_asks, "no_asks": no_asks}