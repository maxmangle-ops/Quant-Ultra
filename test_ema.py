from indicators.ema import calculate_ema

prices = [
    100,101,102,103,104,
    105,106,107,108,109,
    110,111,112,113,114,
    115,116,117,118,119
]

ema20 = calculate_ema(prices, 20)

print(ema20)