"""
=========================================================
QUANT ULTRA
Instrument Manager
=========================================================
Central registry for every tradable instrument.

Everything else in Quant Ultra asks THIS module
about symbols instead of hardcoding values.
=========================================================
"""

from dataclasses import dataclass


# =========================================================
# Instrument
# =========================================================

@dataclass
class Instrument:

    symbol: str

    exchange: str

    instrument_key: str

    asset_type: str

    lot_size: int

    tick_size: float


# =========================================================
# Instrument Manager
# =========================================================

class InstrumentManager:

    def __init__(self):

        self.instruments = {

            "NIFTY": Instrument(

                symbol="NIFTY",

                exchange="NSE",

                instrument_key="NSE_INDEX|Nifty 50",

                asset_type="INDEX",

                lot_size=75,

                tick_size=0.05,

            ),

            "BANKNIFTY": Instrument(

                symbol="BANKNIFTY",

                exchange="NSE",

                instrument_key="NSE_INDEX|Nifty Bank",

                asset_type="INDEX",

                lot_size=35,

                tick_size=0.05,

            ),

            "SENSEX": Instrument(

                symbol="SENSEX",

                exchange="BSE",

                instrument_key="BSE_INDEX|SENSEX",

                asset_type="INDEX",

                lot_size=20,

                tick_size=0.05,

            ),

            "INFY": Instrument(

                symbol="INFY",

                exchange="NSE",

                instrument_key="NSE_EQ|INE009A01021",

                asset_type="EQUITY",

                lot_size=1,

                tick_size=0.05,

            ),

        }

    # -------------------------------------------------

    def get(self, symbol):

        symbol = symbol.upper()

        return self.instruments.get(symbol)

    # -------------------------------------------------

    def exists(self, symbol):

        return symbol.upper() in self.instruments

    # -------------------------------------------------

    def all(self):

        return list(self.instruments.values())


# ---------------------------------------------------------

if __name__ == "__main__":

    manager = InstrumentManager()

    instrument = manager.get("NIFTY")

    print()

    print("=" * 60)

    print("INSTRUMENT MANAGER")

    print("=" * 60)

    print(instrument)