from margin.calculator import MarginEngine

engine = MarginEngine()

result = engine.calculate(
    available_margin=20000,
    required_margin=18500,
)

print()

print("=" * 45)
print("💰 MARGIN ENGINE")
print("=" * 45)

print(f"Approved      : {result.approved}")
print(f"Status        : {result.status}")
print(f"Utilization   : {result.utilization}%")
print(f"Remaining     : ₹{result.remaining_margin}")
print(f"Recommendation: {result.recommendation}")

print("=" * 45)