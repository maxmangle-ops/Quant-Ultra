"""
=========================================================
QUANT ULTRA
Backtest Engine
=========================================================
"""

import pandas as pd

from engine.live_analyzer import analyze


class BacktestEngine:

    def __init__(self):

        self.total_trades = 0

        self.wins = 0

        self.losses = 0

        self.net_profit = 0

        self.trade_log = []

    # -------------------------------------------------

    def run(

        self,

        symbol,

        timeframe="5minute",

    ):

        print()

        print("=" * 60)

        print("📊 QUANT ULTRA BACKTEST")

        print("=" * 60)

        analysis = analyze(

            symbol=symbol,

            timeframe=timeframe,

        )

        print()

        print("Latest Analysis")

        print()

        for key, value in analysis.items():

            print(f"{key:20}: {value}")

        print()

        print("⚠ Full historical simulation coming in v2.")

    # -------------------------------------------------

    def record_trade(

        self,

        pnl,

    ):

        self.total_trades += 1

        self.net_profit += pnl

        self.trade_log.append(pnl)

        if pnl >= 0:

            self.wins += 1

        else:

            self.losses += 1

    # -------------------------------------------------

    def summary(self):

        if self.total_trades == 0:

            win_rate = 0

        else:

            win_rate = (

                self.wins

                / self.total_trades

            ) * 100

        print()

        print("=" * 60)

        print("📈 BACKTEST SUMMARY")

        print("=" * 60)

        print(f"Trades      : {self.total_trades}")

        print(f"Wins        : {self.wins}")

        print(f"Losses      : {self.losses}")

        print(f"Win Rate    : {win_rate:.2f}%")

        print(f"Net Profit  : ₹{self.net_profit:.2f}")

        print("=" * 60)


# ---------------------------------------------------------

if __name__ == "__main__":

    engine = BacktestEngine()

    engine.run(

        symbol="INFY",

        timeframe="5minute",

    )