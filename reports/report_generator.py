"""
=========================================================
QUANT ULTRA
Daily Report Generator
=========================================================
"""

from datetime import datetime
from pathlib import Path
import csv


class ReportGenerator:

    def __init__(self):

        self.report_folder = Path("reports")

        self.report_folder.mkdir(

            exist_ok=True

        )

    # -------------------------------------------------

    def generate(

        self,

        trades,

        account,

    ):

        today = datetime.now().strftime(

            "%Y%m%d"

        )

        filename = self.report_folder / f"{today}.csv"

        total_pnl = sum(

            trade.get(

                "pnl",

                0,

            )

            for trade in trades

        )

        wins = len(

            [

                t

                for t in trades

                if t.get(

                    "pnl",

                    0,

                ) > 0

            ]

        )

        losses = len(trades) - wins

        with open(

            filename,

            "w",

            newline="",

        ) as file:

            writer = csv.writer(file)

            writer.writerow(

                [

                    "Date",

                    datetime.now(),

                ]

            )

            writer.writerow([])

            writer.writerow(

                [

                    "Starting Capital",

                    account["starting_capital"],

                ]

            )

            writer.writerow(

                [

                    "Ending Capital",

                    account["ending_capital"],

                ]

            )

            writer.writerow(

                [

                    "Net PnL",

                    total_pnl,

                ]

            )

            writer.writerow(

                [

                    "Wins",

                    wins,

                ]

            )

            writer.writerow(

                [

                    "Losses",

                    losses,

                ]

            )

            writer.writerow([])

            writer.writerow(

                [

                    "Symbol",

                    "Side",

                    "Entry",

                    "Exit",

                    "Quantity",

                    "PnL",

                    "Status",

                ]

            )

            for trade in trades:

                writer.writerow(

                    [

                        trade["symbol"],

                        trade["side"],

                        trade["entry"],

                        trade["exit"],

                        trade["quantity"],

                        trade["pnl"],

                        trade["status"],

                    ]

                )

        print()

        print("=" * 60)

        print("📊 DAILY REPORT GENERATED")

        print("=" * 60)

        print(filename)

        print("=" * 60)

        return filename


# ---------------------------------------------------------

if __name__ == "__main__":

    report = ReportGenerator()

    trades = [

        {

            "symbol":"NIFTY",

            "side":"BUY",

            "entry":25100,

            "exit":25220,

            "quantity":1,

            "pnl":120,

            "status":"CLOSED",

        },

        {

            "symbol":"BANKNIFTY",

            "side":"SELL",

            "entry":57000,

            "exit":57150,

            "quantity":1,

            "pnl":-150,

            "status":"CLOSED",

        },

    ]

    account = {

        "starting_capital":10000,

        "ending_capital":9970,

    }

    report.generate(

        trades,

        account,

    )