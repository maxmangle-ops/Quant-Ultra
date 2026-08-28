import pandas as pd


def calculate_vwap(high, low, close, volume, time):
    df = pd.DataFrame({
        "time": time,
        "high": high,
        "low": low,
        "close": close,
        "volume": volume
    })

    # Extract trading date
    df["date"] = pd.to_datetime(df["time"]).dt.date

    # Typical Price
    df["tp"] = (df["high"] + df["low"] + df["close"]) / 3

    # Price × Volume
    df["tpv"] = df["tp"] * df["volume"]

    # Reset VWAP every day
    df["cum_tpv"] = df.groupby("date")["tpv"].cumsum()
    df["cum_vol"] = df.groupby("date")["volume"].cumsum()

    return df["cum_tpv"] / df["cum_vol"]