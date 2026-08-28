import pandas as pd
from indicators.vwap import calculate_vwap

data = pd.DataFrame({
    "high": [10,11,12,13,14],
    "low": [9,10,11,12,13],
    "close": [9.5,10.5,11.5,12.5,13.5],
    "volume": [100,120,110,130,140]
})

vwap = calculate_vwap(
    data["high"],
    data["low"],
    data["close"],
    data["volume"]
)

print(vwap)