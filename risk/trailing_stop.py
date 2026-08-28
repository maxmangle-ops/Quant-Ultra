"""
=========================================================
QUANT ULTRA
Trailing Stop Engine
=========================================================
"""

from config.settings import ATR_TRAILING_MULTIPLIER


class TrailingStopEngine:

    def __init__(self):

        pass

    # -------------------------------------------------

    def update(

        self,

        position,

        current_price,

        atr,

    ):

        stop_loss = position["stop_loss"]

        side = position["side"]

        changed = False

        # -----------------------------------------
        # BUY Position
        # -----------------------------------------

        if side == "BUY":

            new_stop = current_price - (
                atr * ATR_TRAILING_MULTIPLIER
            )

            if new_stop > stop_loss:

                stop_loss = round(new_stop, 2)

                changed = True

        # -----------------------------------------
        # SELL Position
        # -----------------------------------------

        else:

            new_stop = current_price + (
                atr * ATR_TRAILING_MULTIPLIER
            )

            if new_stop < stop_loss:

                stop_loss = round(new_stop, 2)

                changed = True

        return {

            "changed": changed,

            "stop_loss": stop_loss,

        }


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    engine = TrailingStopEngine()

    position = {

        "side": "BUY",

        "stop_loss": 24950,

    }

    result = engine.update(

        position,

        current_price=25090,

        atr=20,

    )

    print()

    print("=" * 55)

    print("📈 TRAILING STOP")

    print("=" * 55)

    print(result)