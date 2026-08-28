from indicators.rsi import calculate_rsi

prices = [
    100,101,102,103,104,
    105,106,107,108,109,
    110,111,112,113,114,
    115,116,117,118,119
]

rsi = calculate_rsi(prices)

print(rsi)