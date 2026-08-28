from strategy.signal_engine import generate_signal


def analyze_market(price, ema20, ema50, rsi, atr, vwap):
    signal = generate_signal(
        price=price,
        ema20=ema20,
        ema50=ema50,
        rsi=rsi,
        atr=atr,
        vwap=vwap
    )

    print("\n==============================")
    print("📈 QUANT ULTRA")
    print("==============================")
    print(f"Price  : ₹{price:.2f}")
    print(f"EMA20  : {ema20:.2f}")
    print(f"EMA50  : {ema50:.2f}")
    print(f"RSI14  : {rsi:.2f}")
    print(f"ATR14  : {atr:.2f}")
    print(f"VWAP   : {vwap:.2f}")
    print(f"Signal : {signal}")
    print("==============================")