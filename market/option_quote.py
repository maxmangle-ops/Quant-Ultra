"""
=========================================================
QUANT ULTRA
Option Quote Engine
=========================================================
Fetches Live Option Premium
=========================================================
"""

import os

import upstox_client

from dotenv import load_dotenv


class OptionQuoteEngine:

    def __init__(self):

        load_dotenv()

        configuration = upstox_client.Configuration()

        configuration.access_token = os.getenv(
            "UPSTOX_ACCESS_TOKEN"
        )

        api_client = upstox_client.ApiClient(
            configuration
        )

        self.api = upstox_client.MarketQuoteApi(
            api_client
        )

    # -------------------------------------------------

    def get_ltp(

        self,

        instrument_key,

    ):

        response = self.api.ltp(

            symbol=instrument_key,

            api_version="2.0",

        )

        data = response.data

        if not data:

            return None

        first = next(iter(data.values()))

        return first.last_price


# ---------------------------------------------------------

if __name__ == "__main__":

    engine = OptionQuoteEngine()

    premium = engine.get_ltp(

        "NSE_FO|63949"

    )

    print()

    print("=" * 60)

    print("OPTION QUOTE ENGINE")

    print("=" * 60)

    print("Premium :", premium)