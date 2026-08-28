"""
=========================================================
QUANT ULTRA
Daily Risk Guard
=========================================================
Protects account from overtrading and excessive losses.
=========================================================
"""

from datetime import date

from config.settings import (
    MAX_DAILY_LOSS_PERCENT,
    MAX_DAILY_PROFIT_PERCENT,
    MAX_CONSECUTIVE_LOSSES,
)


class DailyGuard:

    def __init__(self):

        self.reset()

    # -------------------------------------------------

    def reset(self):

        self.day = date.today()

        self.daily_pnl = 0.0

        self.consecutive_losses = 0

        self.trades = 0

        self.trading_allowed = True

    # -------------------------------------------------

    def new_day(self):

        if self.day != date.today():

            self.reset()

    # -------------------------------------------------

    def update(

        self,

        pnl,

        account_size,

    ):

        self.new_day()

        self.trades += 1

        self.daily_pnl += pnl

        if pnl < 0:

            self.consecutive_losses += 1

        else:

            self.consecutive_losses = 0

        daily_loss_limit = (
            account_size
            * MAX_DAILY_LOSS_PERCENT
            / 100
        )

        daily_profit_limit = (
            account_size
            * MAX_DAILY_PROFIT_PERCENT
            / 100
        )

        reason = None

        # ---------------------------------------------
        # Daily Loss Limit
        # ---------------------------------------------

        if self.daily_pnl <= -daily_loss_limit:

            self.trading_allowed = False

            reason = "Maximum Daily Loss Reached"

        # ---------------------------------------------
        # Daily Profit Target
        # ---------------------------------------------

        elif self.daily_pnl >= daily_profit_limit:

            self.trading_allowed = False

            reason = "Daily Target Achieved"

        # ---------------------------------------------
        # Consecutive Losses
        # ---------------------------------------------

        elif (

            self.consecutive_losses

            >= MAX_CONSECUTIVE_LOSSES

        ):

            self.trading_allowed = False

            reason = "Maximum Consecutive Losses"

        return {

            "allowed": self.trading_allowed,

            "daily_pnl": round(

                self.daily_pnl,

                2,

            ),

            "trades": self.trades,

            "loss_streak": self.consecutive_losses,

            "reason": reason,

        }


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    guard = DailyGuard()

    account = 10000

    trades = [

        -120,

        -150,

        -180,

        300,

    ]

    print()

    print("=" * 60)

    print("🛡 DAILY GUARD")

    print("=" * 60)

    for pnl in trades:

        report = guard.update(

            pnl,

            account,

        )

        print(report)

        if not report["allowed"]:

            break