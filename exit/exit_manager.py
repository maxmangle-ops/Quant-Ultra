"""
=========================================================
QUANT ULTRA
Exit Manager
=========================================================
"""

from datetime import datetime


class ExitManager:

    def __init__(self):

        pass

    # -----------------------------------------------------
    # Evaluate Exit
    # -----------------------------------------------------

    def evaluate(self, position, ltp):

        result = {

            "exit": False,

            "reason": None,

            "exit_price": None,

            "pnl": 0,

        }

        entry = position["entry"]

        stop_loss = position["stop_loss"]

        target = position["target"]

        quantity = position["quantity"]

        side = position["side"]

        # ---------------------------------------------
        # BUY Position
        # ---------------------------------------------

        if side == "BUY":

            if ltp <= stop_loss:

                result["exit"] = True
                result["reason"] = "STOP LOSS"

            elif ltp >= target:

                result["exit"] = True
                result["reason"] = "TARGET"

        # ---------------------------------------------
        # SELL Position
        # ---------------------------------------------

        else:

            if ltp >= stop_loss:

                result["exit"] = True
                result["reason"] = "STOP LOSS"

            elif ltp <= target:

                result["exit"] = True
                result["reason"] = "TARGET"

        # ---------------------------------------------
        # Exit Calculation
        # ---------------------------------------------

        if result["exit"]:

            result["exit_price"] = round(ltp, 2)

            if side == "BUY":

                pnl = (

                    ltp - entry

                ) * quantity

            else:

                pnl = (

                    entry - ltp

                ) * quantity

            result["pnl"] = round(pnl, 2)

            result["time"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        return result


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    manager = ExitManager()

    trade = {

        "symbol": "NIFTY",

        "side": "BUY",

        "entry": 25000,

        "stop_loss": 24950,

        "target": 25100,

        "quantity": 1,

    }

    print()

    print("=" * 60)

    print("EXIT TEST")

    print("=" * 60)

    print(manager.evaluate(trade, 25105))