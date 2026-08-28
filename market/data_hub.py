"""
=========================================================
QUANT ULTRA
Data Hub
=========================================================
Single source of truth for all market/account data.
=========================================================
"""

from datetime import datetime

from market.historical import get_historical_dataframe


class DataHub:

    def __init__(self):

        self.market = {}

        self.account = {}

        self.option_chain = {}

        self.guardian = {}

        self.positions = []

        self.orders = []

    # -------------------------------------------------
    # Market
    # -------------------------------------------------

    def load_market(self):

        df = get_historical_dataframe()

        latest = df.iloc[-1]

        self.market = {

            "symbol": "INFY",

            "price": float(latest["close"]),

            "high": float(latest["high"]),

            "low": float(latest["low"]),

            "volume": int(latest["volume"]),

            "timestamp": str(latest["time"]),

        }

        return self.market

    # -------------------------------------------------
    # Account
    # -------------------------------------------------

    def load_account(

        self,

        account_dict,

    ):

        self.account = account_dict

        return self.account

    # -------------------------------------------------
    # Option Chain
    # -------------------------------------------------

    def load_option_chain(

        self,

        option_chain_dict,

    ):

        self.option_chain = option_chain_dict

        return self.option_chain

    # -------------------------------------------------
    # Guardian
    # -------------------------------------------------

    def load_guardian(

        self,

        guardian_dict,

    ):

        self.guardian = guardian_dict

        return self.guardian

    # -------------------------------------------------
    # Positions
    # -------------------------------------------------

    def load_positions(

        self,

        positions,

    ):

        self.positions = positions

    # -------------------------------------------------
    # Orders
    # -------------------------------------------------

    def load_orders(

        self,

        orders,

    ):

        self.orders = orders

    # -------------------------------------------------
    # Dashboard
    # -------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 60)

        print("📊 QUANT ULTRA DATA HUB")

        print("=" * 60)

        print()

        print("Market")

        print(self.market)

        print()

        print("Account")

        print(self.account)

        print()

        print("Guardian")

        print(self.guardian)

        print()

        print("Option Chain")

        print(self.option_chain)

        print()

        print(f"Positions : {len(self.positions)}")

        print(f"Orders    : {len(self.orders)}")

        print()

        print("Updated :", datetime.now())

        print("=" * 60)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    hub = DataHub()

    hub.load_market()

    hub.dashboard()