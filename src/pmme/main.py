from kalshi import list_markets_by_series, get_orderbook

markets = list_markets_by_series("KXBTCD", limit=50)
print(f"Found {len(markets)} markets in series")

for m in markets:
    print(m["ticker"], m["yes_ask_dollars"], m["yes_bid_dollars"], m["status"])

from kalshi import list_markets_by_series, get_orderbook

markets = list_markets_by_series("KXBTCD", limit=50)
ticker = markets[0]["ticker"]
print("Using ticker:", ticker)

book = get_orderbook(ticker)
print(book)

from kalshi import list_markets_by_series, derive_ask_levels

markets = list_markets_by_series("KXBTCD", limit=50)

for m in markets:
    ticker = m["ticker"]
    levels = derive_ask_levels(ticker)
    yes_asks, no_asks = levels["yes_asks"], levels["no_asks"]

    if not yes_asks or not no_asks:
        continue  # one-sided market, skip

    gross_edge = 1.0 - (yes_asks[0][0] + no_asks[0][0])
    print(f"{ticker}: YES ask={yes_asks[0][0]}, NO ask={no_asks[0][0]}, gross edge={gross_edge:.4f}")