from market.historical import get_historical_dataframe

df = get_historical_dataframe()

print(df.tail())
print()

print("Rows:", len(df))