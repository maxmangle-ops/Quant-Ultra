import pandas as pd


def calculate_rsi(prices, period=14):
    """
    Calculate Relative Strength Index (RSI)

    prices : list or pandas Series
    period : RSI period (default 14)
    """

    prices = pd.Series(prices)

    delta = prices.diff()

    gain = delta.where(delta > 0, 0)

    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi