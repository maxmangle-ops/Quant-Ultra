"""
=========================================================
QUANT ULTRA
Partial Exit Engine
=========================================================
"""

from config.settings import PARTIAL_BOOKING_PERCENT


class PartialExitEngine:

    def __init__(self):
        pass

    # -------------------------------------------------
    # Partial Exit
    # -------------------------------------------------

    def evaluate(self, position, current_price):

        quantity = position["quantity"]

        target = position["target"]

        side = position["side"]

        already_booked = position.get(
            "partial_booked",
            False
        )

        if already_booked:

            return {
                "exit": False,
                "quantity": 0,
                "reason": None,
            }

        if side == "BUY":

            if current_price >= target:

                exit_qty = max(
                    1,
                    int(
                        quantity
                        * PARTIAL_BOOKING_PERCENT
                        / 100
                    )
                )

                return {

                    "exit": True,

                    "quantity": exit_qty,

                    "reason": "TARGET-1",

                }

        else:

            if current_price <= target:

                exit_qty = max(
                    1,
                    int(
                        quantity
                        * PARTIAL_BOOKING_PERCENT
                        / 100
                    )
                )

                return {

                    "exit": True,

                    "quantity": exit_qty,

                    "reason": "TARGET-1",

                }

        return {

            "exit": False,

            "quantity": 0,

            "reason": None,

        }


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    engine = PartialExitEngine()

    trade = {

        "quantity": 4,

        "target": 25080,

        "side": "BUY",

    }

    result = engine.evaluate(

        trade,

        current_price=25090,

    )

    print()

    print("=" * 55)

    print("💰 PARTIAL EXIT")

    print("=" * 55)

    print(result)