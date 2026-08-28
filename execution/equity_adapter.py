"""
=========================================================
QUANT ULTRA
Equity Adapter
=========================================================
Converts Equity Analysis into TradePlan.
=========================================================
"""

from risk.risk_manager import calculate_position


class EquityAdapter:

    def __init__(self):
        pass

    # -------------------------------------------------

    def create_trade(

        self,

        analysis,

        capital,

        risk_percent,

    ):

        return calculate_position(

            entry_price=analysis["price"],

            atr=analysis["atr"],

            available_cash=capital,

            buying_power=capital * 5,

            risk_percent=risk_percent,

            profile="BALANCED",

        )


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("EQUITY ADAPTER READY")

    print("=" * 60)