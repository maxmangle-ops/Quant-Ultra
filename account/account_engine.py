"""
=========================================================
QUANT ULTRA
Account Engine
=========================================================
"""

import os

import upstox_client

from account.account_models import Account
from config.settings import BROKER_NAME


class AccountEngine:

    def __init__(self):

        configuration = upstox_client.Configuration()

        configuration.access_token = os.getenv(
            "UPSTOX_ACCESS_TOKEN"
        )

        self.client = upstox_client.ApiClient(
            configuration
        )

    # -----------------------------------------------------
    # Fetch Account
    # -----------------------------------------------------

    def fetch(self) -> Account:

        """
        Returns current account details.

        NOTE:
        Currently returns demo values.

        Later this method will call
        Upstox Fund & Margin APIs.
        """

        return Account(

            broker=BROKER_NAME,

            available_cash=20000,

            available_margin=19500,

            used_margin=500,

            buying_power=100000,

            pnl_today=250,

            open_positions=1,

            holdings=3,

            open_orders=2,
        )

    # -----------------------------------------------------
    # Health Check
    # -----------------------------------------------------

    def health(self):

        try:

            if self.client:

                return True

        except Exception:

            return False

        return False