from src.pmme.kalshi import list_open_markets

markets = list_open_markets(limit=300)

two_sided = [
    m for m in markets
    if "MVE" not in m["ticker"]
    and m["yes_ask_dollars"] != "0.0000"
    and m["yes_bid_dollars"] != "0.0000"
]

print(f"Found {len(two_sided)} two-sided markets out of {len(markets)}")
for m in two_sided[:10]:
    print(m["ticker"], m["yes_bid_dollars"], m["yes_ask_dollars"], m["title"])