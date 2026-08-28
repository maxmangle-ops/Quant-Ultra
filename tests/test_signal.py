from strategy.signal_engine import generate_signal

signal = generate_signal(
    price=1090,
    ema20=1089,
    ema50=1088,
    rsi=62,
    vwap=1088.5,
    atr=1.5
)

print(signal)