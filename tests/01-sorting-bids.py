from src.pmme.kalshi import derive_ask_levels

levels = derive_ask_levels("KXBTCD-26SEP1616-T85799.99")
print("YES asks (cheapest first):", levels["yes_asks"][:3])
print("NO asks (cheapest first):", levels["no_asks"][:3])