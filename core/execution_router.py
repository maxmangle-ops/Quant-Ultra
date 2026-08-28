"""
=========================================================
QUANT ULTRA
Execution Router
=========================================================
Chooses whether to trade Equity or Options.
=========================================================
"""

from enum import Enum


class ExecutionType(Enum):

    EQUITY = "EQUITY"

    OPTIONS = "OPTIONS"

    FUTURES = "FUTURES"


class ExecutionRouter:

    def __init__(self):
        pass

    # -------------------------------------------------

    def decide(

        self,

        capital,

        technical_score,

        market_regime=None,

        volatility=None,

    ):

        # -------------------------------------------------
        # Low Capital
        # -------------------------------------------------

        if capital < 100000:

            return ExecutionType.OPTIONS

        # -------------------------------------------------
        # High Volatility
        # -------------------------------------------------

        if volatility is not None:

            if volatility > 25:

                return ExecutionType.OPTIONS

        # -------------------------------------------------
        # Strong Trend
        # -------------------------------------------------

        if technical_score >= 80:

            return ExecutionType.EQUITY

        # -------------------------------------------------

        return ExecutionType.EQUITY


# ---------------------------------------------------------

if __name__ == "__main__":

    router = ExecutionRouter()

    print()

    print("=" * 60)

    print("EXECUTION ROUTER")

    print("=" * 60)

    print(

        router.decide(

            capital=10000,

            technical_score=70,

        )

    )

    print(

        router.decide(

            capital=300000,

            technical_score=85,

        )

    )