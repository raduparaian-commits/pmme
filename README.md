# Prediction Market Mispricing Engine

PMME detects mispricing in binary prediction markets (Polymarket & Kalshi) and
sizes positions against the real, cost-adjusted edge, after fees, spread, slippage, and gas eat most of it.

## The core idea

Every binary contract resolves to exactly one outcome, YES or NO.
Buying both sides guarantees a $1 payout at resolution no matter what
happens, so

```
edge = 1 - (yes_ask + no_ask)
```

Two places to check this:

- **Same-venue**: YES ask + NO ask on the same contract, same order book.
- **Cross-venue**: The same real-world event listed on both Polymarket and
  Kalshi, priced differently.

Detection is the easy part, it's a couple of API calls and one line of
math. The actual project is what happens *after* detection: subtracting
trading fees, the spread you cross, slippage from walking the book past
top-of-book depth, and (for Polymarket) gas — then sizing the survivors
with fractional Kelly. Most of what looks like edge dies at that stage.

A 2026 UCLA paper ("Arbitrage Analysis in Polymarket NBA Markets," Cheng,
Yang & Zou) analyzing 75M Polymarket order book snapshots across 173 NBA
games found only **7 executable single-market arbitrages**, each alive for
~3.6 seconds, with realized executable size bottlenecked to a median of
~15 shares by thin depth. That's the honest baseline expectation for this
project — rare, fast-closing, small.

## Status

This is a work in progress, built incrementally rather than all at once.

- [x] Kalshi market discovery (`/markets`, filtered/paginated)
- [x] Kalshi order book fetch
- [x] Derive YES/NO ask levels from Kalshi's bid-only order book
- [x] Same-venue gross edge check (top-of-book)
- [ ] Book-walking / slippage-aware fill simulation
- [ ] Fee model (Kalshi + Polymarket)
- [ ] Net edge (gross − fees − slippage − gas)
- [ ] Polymarket client (CLOB order book)
- [ ] Cross-venue event matching
- [ ] Kelly sizing
- [ ] Continuous polling loop + logging
- [ ] Execution layer (paper-traded first)

## Setup

```bash
uv init .
uv add requests
```

No API keys needed yet, Kalshi's market data endpoints are public for
reads. Keys only become necessary once order placement is built.

```bash
uv run main.py
```

## Roadmap notes

- Cross-venue matching is the hardest part of this project because there is no shared ID
  between Polymarket and Kalshi markets, and is intentionally deferred
  until same-venue detection and the cost model are solid.
- Execution will be paper-traded before any real order placement.

## Disclaimer

This project detects and analyzes prices; it is not financial advice and
does not place real trades. Before running it against live accounts, read
Kalshi's and Polymarket's API Terms of Service, rate limits, automated
trading rules, and jurisdiction restrictions apply and vary by venue.
