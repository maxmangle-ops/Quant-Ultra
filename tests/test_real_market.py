from market.historical import get_historical_dataframe

from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.atr import calculate_atr
from indicators.vwap import calculate_vwap

df = get_historical_dataframe()

# Indicators
df["EMA20"] = calculate_ema(df["close"], 20)
df["EMA50"] = calculate_ema(df["close"], 50)

df["RSI14"] = calculate_rsi(df["close"])

df["ATR14"] = calculate_atr(
    df["high"],
    df["low"],
    df["close"]
)

df["VWAP"] = calculate_vwap(
    df["high"],
    df["low"],
    df["close"],
    df["volume"]
)

print("\n========== LATEST MARKET DATA ==========\n")

print(df.tail(10))

print("\nLatest Candle:\n")

print(df.iloc[-1])