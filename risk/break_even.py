"""
=========================================================
QUANT ULTRA
Break Even Engine
=========================================================
"""

from config.settings import BREAK_EVEN_TRIGGER


class BreakEvenEngine:

    def __init__(self):
        pass

    # -------------------------------------------------

    def update(
        self,
        position,
        current_price,
        atr,
    ):

        side = position["side"]

        entry = position["entry"]

        stop_loss = position["stop_loss"]

        trigger = atr * BREAK_EVEN_TRIGGER

        changed = False

        # -----------------------------------------
        # BUY
        # -----------------------------------------

        if side == "BUY":

            if current_price >= entry + trigger:

                if stop_loss < entry:

                    stop_loss = round(entry, 2)

                    changed = True

        # -----------------------------------------
        # SELL
        # -----------------------------------------

        else:

            if current_price <= entry - trigger:

                if stop_loss > entry:

                    stop_loss = round(entry, 2)

                    changed = True

        return {

            "changed": changed,

            "stop_loss": stop_loss,

            "reason": "Break Even Activated" if changed else None,

        }


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    engine = BreakEvenEngine()

    trade = {

        "side": "BUY",

        "entry": 25000,

        "stop_loss": 24950,

    }

    result = engine.update(

        position=trade,

        current_price=25035,

        atr=20,

    )

    print()

    print("=" * 55)

    print("💰 BREAK EVEN ENGINE")

    print("=" * 55)

    print(result)