"""
=========================================================
QUANT ULTRA
Performance Report Engine
=========================================================
"""

import csv
import os

from config.settings import JOURNAL_FILE


class PerformanceReport:

    def __init__(self):

        self.trades = []

        self.load()

    # -------------------------------------------------

    def load(self):

        self.trades = []

        if not os.path.exists(JOURNAL_FILE):

            return

        with open(JOURNAL_FILE, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                self.trades.append(row)

    # -------------------------------------------------

    def summary(self):

        total = len(self.trades)

        wins = 0
        losses = 0

        gross_profit = 0.0
        gross_loss = 0.0

        best_trade = 0.0
        worst_trade = 0.0

        for trade in self.trades:

            pnl = float(trade["PnL"] or 0)

            if pnl > 0:

                wins += 1

                gross_profit += pnl

            elif pnl < 0:

                losses += 1

                gross_loss += abs(pnl)

            if pnl > best_trade:

                best_trade = pnl

            if pnl < worst_trade:

                worst_trade = pnl

        net = gross_profit - gross_loss

        win_rate = 0

        if total:

            win_rate = round((wins / total) * 100, 2)

        avg_profit = 0

        if wins:

            avg_profit = gross_profit / wins

        avg_loss = 0

        if losses:

            avg_loss = gross_loss / losses

        profit_factor = 0

        if gross_loss:

            profit_factor = round(
                gross_profit / gross_loss,
                2
            )

        return {

            "Total Trades": total,

            "Winning Trades": wins,

            "Losing Trades": losses,

            "Win Rate": f"{win_rate}%",

            "Gross Profit": round(gross_profit, 2),

            "Gross Loss": round(gross_loss, 2),

            "Net Profit": round(net, 2),

            "Average Win": round(avg_profit, 2),

            "Average Loss": round(avg_loss, 2),

            "Profit Factor": profit_factor,

            "Best Trade": round(best_trade, 2),

            "Worst Trade": round(worst_trade, 2),
        }

    # -------------------------------------------------

    def print_report(self):

        report = self.summary()

        print()

        print("=" * 60)

        print("📊 QUANT ULTRA PERFORMANCE REPORT")

        print("=" * 60)

        for key, value in report.items():

            print(f"{key:20}: {value}")

        print("=" * 60)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    report = PerformanceReport()

    report.print_report()