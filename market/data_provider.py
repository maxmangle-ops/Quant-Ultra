import pandas as pd

candles = []


def add_candle(candle):
    candles.append(candle)

    # Keep only last 100 candles
    if len(candles) > 100:
        candles.pop(0)


def get_dataframe():
    return pd.DataFrame(candles)