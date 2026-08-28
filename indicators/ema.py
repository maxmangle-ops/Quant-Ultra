import pandas as pd


def calculate_ema(prices, period):
    """
    Calculate Exponential Moving Average.

    prices : list or pandas Series
    period : EMA period (e.g. 20, 50)
    """

    series = pd.Series(prices)

    ema = series.ewm(span=period, adjust=False).mean()

    return ema