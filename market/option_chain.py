"""
=========================================================
QUANT ULTRA
Option Chain Engine
=========================================================
Downloads option contracts and converts them into
OptionContract dataclass objects.
=========================================================
"""

import os
from datetime import datetime, timedelta

import upstox_client
from dotenv import load_dotenv

from models.option_models import OptionContract

load_dotenv()


class OptionChainEngine:

    def __init__(self):

        configuration = upstox_client.Configuration()
        configuration.access_token = os.getenv(
            "UPSTOX_ACCESS_TOKEN"
        )

        client = upstox_client.ApiClient(configuration)

        self.api = upstox_client.OptionsApi(client)

        self.cache = {}

        self.cache_time = {}

        self.cache_duration = timedelta(minutes=5)

    # -------------------------------------------------

    def get_contracts(self, instrument_key):

        now = datetime.now()

        # ---------------- Cache ----------------

        if instrument_key in self.cache:

            if now - self.cache_time[instrument_key] < self.cache_duration:

                return self.cache[instrument_key]

        # --------------------------------------

        response = self.api.get_option_contracts(
            instrument_key=instrument_key
        )

        contracts = []

        for c in response.data:

            contracts.append(

                OptionContract(

                    instrument_key=c.instrument_key,

                    trading_symbol=c.trading_symbol,

                    strike=c.strike_price,

                    option_type=c.instrument_type,

                    expiry=c.expiry,

                    weekly=c.weekly,

                    lot_size=c.lot_size,

                    exchange=c.exchange,

                    underlying=c.underlying_symbol,

                )

            )

        self.cache[instrument_key] = contracts

        self.cache_time[instrument_key] = now

        return contracts


# ---------------------------------------------------------

if __name__ == "__main__":

    engine = OptionChainEngine()

    contracts = engine.get_contracts(
        "NSE_INDEX|Nifty 50"
    )

    print()

    print("=" * 60)

    print("OPTION CHAIN")

    print("=" * 60)

    print("Contracts :", len(contracts))

    print()

    print(contracts[0])