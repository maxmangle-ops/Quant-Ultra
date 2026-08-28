"""
=========================================================
QUANT ULTRA
Position Calculator
=========================================================
Calculates live position statistics.
=========================================================
"""

from datetime import datetime


class PositionCalculator:

    @staticmethod
    def update(position, ltp):

        now = datetime.now()

        # -----------------------------------------
        # Live Price
        # -----------------------------------------

        position.current_price = ltp
        position.last_updated = now

        position.highest_price = max(
            position.highest_price,
            ltp,
        )

        position.lowest_price = min(
            position.lowest_price,
            ltp,
        )

        # -----------------------------------------
        # PnL
        # -----------------------------------------

        if position.side.upper() == "BUY":

            pnl = (ltp - position.entry) * position.quantity

        else:

            pnl = (position.entry - ltp) * position.quantity

        position.pnl = round(pnl, 2)

        # -----------------------------------------
        # PnL %
        # -----------------------------------------

        investment = position.entry * position.quantity

        if investment > 0:

            position.pnl_percent = round(
                (pnl / investment) * 100,
                2,
            )

        # -----------------------------------------
        # Max Profit / Drawdown
        # -----------------------------------------

        position.max_profit = max(
            position.max_profit,
            position.pnl,
        )

        position.max_drawdown = min(
            position.max_drawdown,
            position.pnl,
        )

        # -----------------------------------------
        # Risk Multiple
        # -----------------------------------------

        risk = abs(
            position.entry - position.stop_loss
        ) * position.quantity

        if risk > 0:

            position.risk_multiple = round(
                pnl / risk,
                2,
            )

        # -----------------------------------------
        # Debug Output (Sprint 2)
        # -----------------------------------------

        print()
        print("=" * 60)
        print("📊 POSITION UPDATED")
        print("=" * 60)
        print(f"Symbol         : {position.symbol}")
        print(f"LTP            : {ltp}")
        print(f"PnL            : ₹{position.pnl}")
        print(f"PnL %          : {position.pnl_percent}%")
        print(f"Max Profit     : ₹{position.max_profit}")
        print(f"Drawdown       : ₹{position.max_drawdown}")
        print(f"Risk Multiple  : {position.risk_multiple} R")
        print("=" * 60)

        return position
