"""
=========================================================
QUANT ULTRA
Portfolio Manager
=========================================================
"""

class PortfolioManager:

    def __init__(self):

        self.positions = []

    # -------------------------------------------------

    def add_position(self, position):

        self.positions.append(position)

    # -------------------------------------------------

    def remove_position(self, position_id):

        self.positions = [

            p for p in self.positions

            if p["position_id"] != position_id

        ]

    # -------------------------------------------------

    def total_capital_used(self):

        return round(

            sum(

                p["capital_used"]

                for p in self.positions

            ),

            2,

        )

    # -------------------------------------------------

    def total_risk(self):

        return round(

            sum(

                p["risk_amount"]

                for p in self.positions

            ),

            2,

        )

    # -------------------------------------------------

    def open_positions(self):

        return len(self.positions)

    # -------------------------------------------------

    def exposure(self):

        exposure = {}

        for position in self.positions:

            symbol = position["symbol"]

            exposure[symbol] = exposure.get(

                symbol,

                0,

            ) + position["capital_used"]

        return exposure

    # -------------------------------------------------

    def direction_exposure(self):

        buy = 0

        sell = 0

        for position in self.positions:

            if position["side"] == "BUY":

                buy += 1

            else:

                sell += 1

        return {

            "BUY": buy,

            "SELL": sell,

        }

    # -------------------------------------------------

    def summary(self):

        print()

        print("=" * 60)

        print("📊 PORTFOLIO")

        print("=" * 60)

        print(

            "Open Positions :",

            self.open_positions()

        )

        print(

            "Capital Used   : ₹",

            self.total_capital_used()

        )

        print(

            "Portfolio Risk : ₹",

            self.total_risk()

        )

        print()

        print("Exposure")

        print(self.exposure())

        print()

        print("Direction")

        print(self.direction_exposure())

        print("=" * 60)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    manager = PortfolioManager()

    manager.add_position({

        "position_id":1,

        "symbol":"NIFTY",

        "side":"BUY",

        "capital_used":25000,

        "risk_amount":500,

    })

    manager.add_position({

        "position_id":2,

        "symbol":"BANKNIFTY",

        "side":"SELL",

        "capital_used":30000,

        "risk_amount":650,

    })

    manager.summary()