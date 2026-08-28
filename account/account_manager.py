"""
=========================================================
QUANT ULTRA
Account Manager
=========================================================
"""

from account.account_models import Account


class AccountManager:

    def __init__(self):

        self._account = None

    # -----------------------------------------------------
    # Update Account
    # -----------------------------------------------------

    def update(self, account: Account):

        self._account = account

    # -----------------------------------------------------
    # Get Account
    # -----------------------------------------------------

    def get(self) -> Account:

        if self._account is None:
            raise RuntimeError(
                "Account not loaded. Call AccountEngine.fetch() first."
            )

        return self._account

    # -----------------------------------------------------
    # Account Loaded?
    # -----------------------------------------------------

    def is_loaded(self):

        return self._account is not None

    # -----------------------------------------------------
    # Print Summary
    # -----------------------------------------------------

    def print_summary(self):

        account = self.get()

        print()
        print("=" * 50)
        print("💼 QUANT ULTRA ACCOUNT")
        print("=" * 50)

        print(f"Broker              : {account.broker}")
        print(f"Available Cash      : ₹{account.available_cash:,.2f}")
        print(f"Available Margin    : ₹{account.available_margin:,.2f}")
        print(f"Used Margin         : ₹{account.used_margin:,.2f}")
        print(f"Buying Power        : ₹{account.buying_power:,.2f}")
        print(f"Today's P&L         : ₹{account.pnl_today:,.2f}")
        print(f"Open Positions      : {account.open_positions}")
        print(f"Holdings            : {account.holdings}")
        print(f"Open Orders         : {account.open_orders}")
        print(f"Margin Utilization  : {account.utilization_percent}%")
        print(f"Last Updated        : {account.last_updated}")

        print("=" * 50)

    # -----------------------------------------------------
    # Convenience Properties
    # -----------------------------------------------------

    @property
    def available_cash(self):

        return self.get().available_cash

    @property
    def available_margin(self):

        return self.get().available_margin

    @property
    def buying_power(self):

        return self.get().buying_power

    @property
    def pnl_today(self):

        return self.get().pnl_today