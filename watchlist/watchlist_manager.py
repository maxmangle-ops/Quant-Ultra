"""
=========================================================
QUANT ULTRA
Watchlist Manager
=========================================================
"""

import json
import os


class WatchlistManager:

    def __init__(self, filepath="data/watchlist.json"):

        self.filepath = filepath

        self.watchlist = []

        self.load()

    # -------------------------------------------------

    def load(self):

        if os.path.exists(self.filepath):

            with open(self.filepath, "r") as file:

                self.watchlist = json.load(file)

        else:

            self.watchlist = []

    # -------------------------------------------------

    def save(self):

        with open(self.filepath, "w") as file:

            json.dump(

                self.watchlist,

                file,

                indent=4,

            )

    # -------------------------------------------------

    def add(self, symbol):

        symbol = symbol.upper()

        if symbol not in self.watchlist:

            self.watchlist.append(symbol)

            self.save()

            print(f"✅ Added {symbol}")

    # -------------------------------------------------

    def remove(self, symbol):

        symbol = symbol.upper()

        if symbol in self.watchlist:

            self.watchlist.remove(symbol)

            self.save()

            print(f"❌ Removed {symbol}")

    # -------------------------------------------------

    def get_symbols(self):

        return self.watchlist

    # -------------------------------------------------

    def clear(self):

        self.watchlist = []

        self.save()

    # -------------------------------------------------

    def show(self):

        print()

        print("=" * 50)

        print("📋 WATCHLIST")

        print("=" * 50)

        for i, symbol in enumerate(

            self.watchlist,

            start=1,

        ):

            print(f"{i}. {symbol}")

        print("=" * 50)


# ---------------------------------------------------------

if __name__ == "__main__":

    manager = WatchlistManager()

    manager.add("NIFTY")

    manager.add("BANKNIFTY")

    manager.add("SENSEX")

    manager.show()