"""
=========================================================
QUANT ULTRA
Trailing Stop Engine
=========================================================
Enhanced Sprint 2 Version
=========================================================
"""


class TrailingStopEngine:

    def calculate(self, position):

        stop = position["stop_loss"]
        entry = position["entry"]
        ltp = position["current_price"]
        atr = position.get("atr", 5)

        milestones = position.setdefault(
            "milestones",
            {
                "breakeven": False,
                "partial1": False,
                "partial2": False,
                "runner": False,
            },
        )

        # -------------------------------------------------
        # Break Even
        # -------------------------------------------------

        if ltp >= entry + atr:

            stop = max(stop, entry)
            milestones["breakeven"] = True

        # -------------------------------------------------
        # ATR Trailing
        # -------------------------------------------------

        if ltp >= entry + (2 * atr):

            stop = max(stop, ltp - atr)
            milestones["runner"] = True

        stop = round(stop, 2)

        print()
        print("=" * 60)
        print("📈 TRAILING STOP ENGINE")
        print("=" * 60)
        print(f"Current Price : {ltp}")
        print(f"ATR           : {atr}")
        print(f"New Stop Loss : {stop}")
        print(f"Breakeven     : {milestones['breakeven']}")
        print(f"Runner Mode   : {milestones['runner']}")
        print("=" * 60)

        return stop


if __name__ == "__main__":

    print()
    print("=" * 60)
    print("TRAILING STOP ENGINE READY")
    print("=" * 60)
