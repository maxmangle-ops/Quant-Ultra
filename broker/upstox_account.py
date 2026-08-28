"""
=========================================================
QUANT ULTRA
Upstox Account Engine
=========================================================
"""

import os

import upstox_client

from dotenv import load_dotenv

load_dotenv()


class UpstoxAccount:

    def __init__(self):

        configuration = upstox_client.Configuration()

        configuration.access_token = os.getenv(
            "UPSTOX_ACCESS_TOKEN"
        )

        self.client = upstox_client.ApiClient(
            configuration
        )

        self.api = upstox_client.UserApi(
            self.client
        )

    # -------------------------------------------------

    def profile(self):

        try:

            profile = self.api.get_profile()

            return profile

        except Exception as e:

            print(e)

            return None

    # -------------------------------------------------

    def funds(self):

        try:

            api = upstox_client.MarginApi(
                self.client
            )

            data = api.get_user_fund_margin()

            return data

        except Exception as e:

            print(e)

            return None

    # -------------------------------------------------

    def positions(self):

        try:

            api = upstox_client.PortfolioApi(
                self.client
            )

            return api.get_positions()

        except Exception as e:

            print(e)

            return None

    # -------------------------------------------------

    def holdings(self):

        try:

            api = upstox_client.PortfolioApi(
                self.client
            )

            return api.get_holdings()

        except Exception as e:

            print(e)

            return None


# ---------------------------------------------------------

if __name__ == "__main__":

    account = UpstoxAccount()

    print()

    print("=" * 60)

    print("UPSTOX PROFILE")

    print("=" * 60)

    print(account.profile())

    print()

    print("=" * 60)

    print("FUNDS")

    print("=" * 60)

    print(account.funds())