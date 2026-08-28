from cost.charges import CostEngine

engine = CostEngine()

result = engine.calculate(
    buy_price=1094.20,
    sell_price=1097.68,
    quantity=574,
)

print()
print("========== COST REPORT ==========")

for key, value in result.items():
    print(f"{key:<15}: {value}")

print("=" * 33)