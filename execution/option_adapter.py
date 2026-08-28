"""
=========================================================
QUANT ULTRA
Option Adapter
=========================================================
Converts Option TradeCandidate into TradePlan.
=========================================================
"""

from market.option_quote import OptionQuoteEngine
from risk.risk_manager import calculate_position


class OptionAdapter:

    def __init__(self):

        self.quote = OptionQuoteEngine()

    # -------------------------------------------------

    def create_trade(

        self,

        candidate,

        capital,

        risk_percent,

        atr=5.0,

        symbol="UNKNOWN",

        side="BUY",

    ):

        premium = self.quote.get_ltp(

            candidate.contract.instrument_key

        )

        if premium is None:

            raise Exception(

                "Unable to fetch option premium."

            )

        trade = calculate_position(

            entry_price=premium,

            atr=atr,

            available_cash=capital,

            buying_power=capital * 5,

            risk_percent=risk_percent,

            profile="BALANCED",

            symbol=symbol,

            side=side,

        )

        return trade


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("OPTION ADAPTER READY")

    print("=" * 60)
