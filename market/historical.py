"""
=========================================================
QUANT ULTRA
Historical Data Provider
=========================================================
"""

import os
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
import upstox_client

from market.candle_builder import build_5minute_dataframe

load_dotenv()

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
history_api = upstox_client.HistoryApi(api_client)


# =========================================================
# Instrument Mapping
# =========================================================

INSTRUMENTS = {

    "INFY": "NSE_EQ|INE009A01021",

    # TODO
    # Replace these with actual Upstox instrument keys

    "NIFTY": "NSE_INDEX|Nifty 50",

    "BANKNIFTY": "NSE_INDEX|Nifty Bank",

    "SENSEX": "BSE_INDEX|SENSEX",

}


# =========================================================
# Historical Data
# =========================================================

def get_historical_dataframe(

    symbol,

    timeframe="1minute",

):

    instrument = INSTRUMENTS.get(

        symbol,

        symbol,

    )

    to_date = datetime.now().strftime("%Y-%m-%d")

    try:

        # --------------------------------------------
        # Upstox does NOT support 5-minute candles.
        # Download 1-minute candles and build 5-minute.
        # --------------------------------------------

        api_interval = timeframe

        if timeframe == "5minute":

            api_interval = "1minute"

        response = history_api.get_historical_candle_data(

            instrument,

            api_interval,

            to_date,

            "2.0",

        )

        candles = response.data.candles

        df = pd.DataFrame(

            candles,

            columns=[

                "time",

                "open",

                "high",

                "low",

                "close",

                "volume",

                "oi",

            ],

        )

        if df.empty:

            return df

        df["time"] = pd.to_datetime(df["time"])

        # Oldest first
        df = df.iloc[::-1].reset_index(drop=True)

        # --------------------------------------------
        # Convert 1-minute candles to 5-minute candles
        # --------------------------------------------

        if timeframe == "5minute":

            df = build_5minute_dataframe(df)

        return df

    except Exception as e:

        print()

        print(f"❌ Historical Data Error [{symbol} | {timeframe}]")

        print(e)

        return pd.DataFrame()


# =========================================================

if __name__ == "__main__":

    df = get_historical_dataframe(

        "INFY",

        "5minute",

    )

    print()

    print(df.head())

    print()

    print(df.tail())

    print()

    print(df.shape)