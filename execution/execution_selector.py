"""
=========================================================
QUANT ULTRA
Execution Selector
=========================================================
Chooses WHICH instrument to trade.
Currently:
    - Options only
Future:
    - Equity
    - Futures
    - ETF
=========================================================
"""

from models.option_models import TradeCandidate


class ExecutionSelector:

    def __init__(self):
        pass

    # -------------------------------------------------

    def choose(

        self,

        analysis,

        capital,

    ):

        direction = "BUY"

        if analysis["trend"] == "BEARISH":
            direction = "SELL"

        # -----------------------------------------
        # Low Capital
        # -----------------------------------------

        if capital <= 100000:

            return {

                "asset_type": "OPTION",

                "underlying": analysis["symbol"],

                "direction": direction,

                "technical_score": analysis["technical_score"],

                "confidence": analysis["confidence"],

            }

        # -----------------------------------------
        # Future Upgrade
        # -----------------------------------------

        return {

            "asset_type": "EQUITY",

            "symbol": analysis["symbol"],

            "direction": direction,

            "technical_score": analysis["technical_score"],

            "confidence": analysis["confidence"],

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    selector = ExecutionSelector()

    trade = selector.choose(

        analysis={

            "symbol": "NIFTY",

            "trend": "BULLISH",

            "technical_score": 82,

            "confidence": 82,

        },

        capital=10000,

    )

    print()

    print("=" * 60)

    print("EXECUTION SELECTOR")

    print("=" * 60)

    print(trade)