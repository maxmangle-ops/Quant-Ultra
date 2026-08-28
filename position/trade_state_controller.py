"""
=========================================================
QUANT ULTRA
Trade State Controller
=========================================================
"""

from core.trade_state import TradeState


class TradeStateController:

    def next_state(

        self,

        position,

    ):

        state = position["state"]

        # -----------------------------
        # ACTIVE
        # -----------------------------

        if state == TradeState.ACTIVE:

            if position["pnl"] > 0:

                return TradeState.PROTECTED

            return TradeState.ACTIVE

        # -----------------------------
        # PROTECTED
        # -----------------------------

        if state == TradeState.PROTECTED:

            if position["health"] >= 90:

                return TradeState.TRAILING

            return TradeState.PROTECTED

        # -----------------------------
        # TRAILING
        # -----------------------------

        if state == TradeState.TRAILING:

            if position["health"] < 50:

                return TradeState.EXIT_PENDING

            return TradeState.TRAILING

        # -----------------------------
        # EXIT
        # -----------------------------

        if state == TradeState.EXIT_PENDING:

            return TradeState.CLOSED

        return state


if __name__ == "__main__":

    print()

    print("=" * 60)

    print("TRADE STATE CONTROLLER READY")

    print("=" * 60)