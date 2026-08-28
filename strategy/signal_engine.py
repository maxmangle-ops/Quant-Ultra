def generate_signal(price, ema20, ema50, rsi, vwap, atr):
    """
    Returns BUY, SELL or WAIT
    """

    if (
        price > ema20
        and ema20 > ema50
        and rsi > 55
        and price > vwap
        and atr > 1
    ):
        return "BUY 🟢"

    if (
        price < ema20
        and ema20 < ema50
        and rsi < 45
        and price < vwap
        and atr > 1
    ):
        return "SELL 🔴"

    return "WAIT 🟡"