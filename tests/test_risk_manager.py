from risk.risk_manager import calculate_position

trade = calculate_position(
    entry_price=1094.20,
    atr=1.74,
    capital=100000,
    risk_percent=1
)

print()

print("===== RISK REPORT =====")

for k, v in trade.items():
    print(f"{k}: {v}")