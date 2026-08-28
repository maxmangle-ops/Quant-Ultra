from datetime import datetime
import pandas as pd

# Per-symbol candle state
current_candles = {}

def update_candle(symbol, price, qty, timestamp):
    """
    Builds independent 5-minute candles per symbol.
    Returns a finished candle dict when a candle closes,
    otherwise returns None.
    """
    global current_candles

    minute = (timestamp.minute // 5) * 5
    candle_time = timestamp.replace(
        minute=minute,
        second=0,
        microsecond=0,
    )

    current = current_candles.get(symbol)

    if current is None:
        current_candles[symbol] = {
            "symbol": symbol,
            "time": candle_time,
            "open": price,
            "high": price,
            "low": price,
            "close": price,
            "volume": qty,
        }
        return None

    if candle_time == current["time"]:
        current["high"] = max(current["high"], price)
        current["low"] = min(current["low"], price)
        current["close"] = price
        current["volume"] += qty
        return None

    finished = current.copy()

    current_candles[symbol] = {
        "symbol": symbol,
        "time": candle_time,
        "open": price,
        "high": price,
        "low": price,
        "close": price,
        "volume": qty,
    }

    return finished


def build_5minute_dataframe(df):

    if df.empty:
        return df

    df = df.copy()
    df["time"] = pd.to_datetime(df["time"])

    df = (
        df.set_index("time")
        .resample("5min")
        .agg(
            {
                "open": "first",
                "high": "max",
                "low": "min",
                "close": "last",
                "volume": "sum",
                "oi": "last",
            }
        )
        .dropna()
        .reset_index()
    )

    return df[
        [
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "oi",
        ]
    ]
