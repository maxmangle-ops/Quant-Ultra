import pandas as pd


def calculate_atr(high, low, close, period=14):
    """
    Calculate Average True Range (ATR)
    """

    high = pd.Series(high)
    low = pd.Series(low)
    close = pd.Series(close)

    prev_close = close.shift(1)

    tr = pd.concat(
        [
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)

    atr = tr.rolling(period).mean()

    return atr