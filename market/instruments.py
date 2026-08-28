"""
=========================================================
QUANT ULTRA
Instrument Manager
=========================================================
"""

import pandas as pd


class InstrumentManager:

    def __init__(self):

        self.instruments = {}

    # -------------------------------------------------
    # Load CSV
    # -------------------------------------------------

    def load_csv(self, filepath):

        df = pd.read_csv(filepath)

        for _, row in df.iterrows():

            symbol = str(row["symbol"]).upper()

            self.instruments[symbol] = {

                "instrument_key": row["instrument_key"],

                "exchange": row["exchange"],

                "name": row["name"],

            }

        print()

        print(f"✅ Loaded {len(self.instruments)} instruments")

    # -------------------------------------------------

    def get_key(self, symbol):

        symbol = symbol.upper()

        if symbol not in self.instruments:

            raise Exception(

                f"Instrument '{symbol}' not found."

            )

        return self.instruments[symbol]["instrument_key"]

    # -------------------------------------------------

    def exists(self, symbol):

        return symbol.upper() in self.instruments

    # -------------------------------------------------

    def search(self, keyword):

        keyword = keyword.upper()

        result = []

        for symbol in self.instruments:

            if keyword in symbol:

                result.append(symbol)

        return result

    # -------------------------------------------------

    def count(self):

        return len(self.instruments)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    manager = InstrumentManager()

    manager.load_csv(

        "data/instruments.csv"

    )

    print()

    print(manager.get_key("INFY"))

    print()

    print(manager.search("NIFTY"))