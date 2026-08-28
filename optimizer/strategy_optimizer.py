"""
=========================================================
QUANT ULTRA
Strategy Optimizer
=========================================================
"""

from statistics import mean


class StrategyOptimizer:

    def __init__(self):

        self.history = {}

    # -------------------------------------------------

    def add_result(

        self,

        strategy,

        pnl,

        win,

    ):

        if strategy not in self.history:

            self.history[strategy] = {

                "trades": 0,

                "wins": 0,

                "losses": 0,

                "pnl": [],

            }

        data = self.history[strategy]

        data["trades"] += 1

        if win:

            data["wins"] += 1

        else:

            data["losses"] += 1

        data["pnl"].append(pnl)

    # -------------------------------------------------

    def report(self):

        print()

        print("=" * 60)

        print("📊 STRATEGY PERFORMANCE")

        print("=" * 60)

        for strategy, data in self.history.items():

            trades = data["trades"]

            wins = data["wins"]

            losses = data["losses"]

            total = sum(data["pnl"])

            average = mean(data["pnl"]) if data["pnl"] else 0

            win_rate = (

                wins / trades * 100

                if trades

                else 0

            )

            print()

            print(f"Strategy : {strategy}")

            print(f"Trades   : {trades}")

            print(f"Wins     : {wins}")

            print(f"Losses   : {losses}")

            print(f"Win Rate : {win_rate:.2f}%")

            print(f"Total PnL: ₹{total:.2f}")

            print(f"Avg Trade: ₹{average:.2f}")

    # -------------------------------------------------

    def best_strategy(self):

        best = None

        best_profit = float("-inf")

        for strategy, data in self.history.items():

            profit = sum(data["pnl"])

            if profit > best_profit:

                best_profit = profit

                best = strategy

        return best


# ---------------------------------------------------------

if __name__ == "__main__":

    optimizer = StrategyOptimizer()

    optimizer.add_result(

        "EMA_RSI_VWAP",

        520,

        True,

    )

    optimizer.add_result(

        "EMA_RSI_VWAP",

        -180,

        False,

    )

    optimizer.add_result(

        "EMA_RSI_VWAP",

        310,

        True,

    )

    optimizer.report()

    print()

    print("🏆 Best Strategy:")

    print(optimizer.best_strategy())