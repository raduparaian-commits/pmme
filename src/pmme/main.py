from kalshi import list_open_markets, get_orderbook

markets = list_open_markets(limit=200)

candidates = [
    m for m in markets
    if "MVE" not in m["ticker"]
    and (m["yes_ask_dollars"] != "0.0000" or m["yes_bid_dollars"] != "0.0000")
]

print(f"Found {len(candidates)} candidates out of {len(markets)} markets")

if not candidates:
    print("Still nothing — printing first 5 raw tickers to see what's actually there")
    for m in markets[:5]:
        print(m["ticker"], m["yes_ask_dollars"], m["yes_bid_dollars"], m["status"])
else:
    ticker = candidates[0]["ticker"]
    print("Using ticker:", ticker)
    book = get_orderbook(ticker)
    print(book)