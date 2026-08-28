"""
=========================================================
QUANT ULTRA
Trade Journal
=========================================================
"""

import csv
import os
from datetime import datetime

from config.settings import JOURNAL_FILE


# ---------------------------------------------------------
# Create Journal
# ---------------------------------------------------------

def initialize_journal():

    folder = os.path.dirname(JOURNAL_FILE)

    if folder:
        os.makedirs(folder, exist_ok=True)

    if os.path.exists(JOURNAL_FILE):
        return

    with open(JOURNAL_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "TradeID",
            "Time",
            "Symbol",
            "Side",
            "Entry",
            "StopLoss",
            "Target",
            "ExitPrice",
            "Quantity",
            "Status",
            "PnL",
        ])


# ---------------------------------------------------------
# Save Trade
# ---------------------------------------------------------

def save_trade(trade):

    initialize_journal()

    with open(JOURNAL_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([

            trade.get("TradeID"),

            trade.get("Time"),

            trade.get("Symbol"),

            trade.get("Side"),

            trade.get("Entry"),

            trade.get("StopLoss"),

            trade.get("Target"),

            trade.get("ExitPrice"),

            trade.get("Quantity"),

            trade.get("Status"),

            trade.get("PnL"),

        ])

    print("💾 Trade Saved")


# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

def get_statistics():

    initialize_journal()

    total = 0

    wins = 0

    losses = 0

    net = 0

    with open(JOURNAL_FILE, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            total += 1

            pnl = float(row["PnL"] or 0)

            net += pnl

            if pnl > 0:
                wins += 1

            elif pnl < 0:
                losses += 1

    if total == 0:

        win_rate = 0

    else:

        win_rate = round((wins / total) * 100, 2)

    return {

        "TotalTrades": total,

        "Wins": wins,

        "Losses": losses,

        "WinRate": win_rate,

        "NetPnL": round(net, 2),

    }


# ---------------------------------------------------------
# Print Statistics
# ---------------------------------------------------------

def print_statistics():

    stats = get_statistics()

    print()

    print("=" * 55)

    print("📊 TRADE JOURNAL")

    print("=" * 55)

    for key, value in stats.items():

        print(f"{key:15}: {value}")

    print("=" * 55)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    initialize_journal()

    print_statistics()