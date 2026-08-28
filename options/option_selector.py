"""
=========================================================
QUANT ULTRA
Option Selector
=========================================================
Selects the best option contract for trading.
=========================================================
"""

from options.atm_selector import ATMSelector
from options.expiry_selector import ExpirySelector
from options.option_score_engine import OptionScoreEngine

from models.option_models import TradeCandidate


class OptionSelector:

    def __init__(self):

        self.atm = ATMSelector()
        self.expiry = ExpirySelector()
        self.scorer = OptionScoreEngine()

    # -------------------------------------------------
    # Strike Step
    # -------------------------------------------------

    def strike_step(self, underlying):

        symbol = underlying.upper()

        if symbol == "BANKNIFTY":
            return 100

        if symbol == "MIDCPNIFTY":
            return 25

        if symbol == "FINNIFTY":
            return 50

        return 50

    # -------------------------------------------------

    def select(

        self,

        contracts,

        spot_price,

        trend,

        technical_score,

        underlying,

    ):

        if not contracts:
            return None

        # -----------------------------------------
        # Step 1 : Nearest Expiry
        # -----------------------------------------

        contracts = self.expiry.select(contracts)

        if not contracts:
            return None

        # -----------------------------------------
        # Step 2 : Strike Step
        # -----------------------------------------

        strike_step = self.strike_step(
            underlying
        )

        # -----------------------------------------
        # Step 3 : ATM Strike
        # -----------------------------------------

        atm = self.atm.nearest_strike(

            spot_price,

            strike_step,

        )

        # -----------------------------------------
        # Step 4 : Option Type
        # -----------------------------------------

        option_type = (

            "CE"

            if trend == "BULLISH"

            else "PE"

        )

        # -----------------------------------------
        # Step 5 : Rank Nearby Contracts
        # -----------------------------------------

        ranked = []

        for contract in contracts:

            if contract.option_type != option_type:
                continue

            distance = abs(
                contract.strike - atm
            )

            # Consider ATM ±2 strikes only
            if distance > strike_step * 2:
                continue

            score, reasons = self.scorer.score(

                contract=contract,

                atm=atm,

                strike_step=strike_step,

                technical_score=technical_score,

            )

            ranked.append(

                (

                    score,

                    reasons,

                    contract,

                )

            )

        if not ranked:
            return None

        ranked.sort(

            key=lambda x: x[0],

            reverse=True,

        )

        best_score, reasons, contract = ranked[0]

        # -----------------------------------------
        # Step 6 : Build Trade Candidate
        # -----------------------------------------

        return TradeCandidate(

            underlying=underlying,

            spot_price=spot_price,

            trend=trend,

            technical_score=technical_score,

            contract=contract,

            confidence=technical_score,

            score=best_score,

            reasons=reasons,

        )


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("OPTION SELECTOR READY")

    print("=" * 60)