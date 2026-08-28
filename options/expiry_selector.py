"""
=========================================================
QUANT ULTRA
Expiry Selector
=========================================================
Selects the most appropriate expiry.
=========================================================
"""

from datetime import datetime, time


class ExpirySelector:

    def __init__(self):
        pass

    # -------------------------------------------------

    def select(self, contracts):

        if not contracts:
            return []

        now = datetime.now()

        today = now.date()

        market_close = time(15, 30)

        expiries = sorted(

            {

                c.expiry.date()

                for c in contracts

            }

        )

        if not expiries:
            return []

        # ---------------------------------------------
        # Before market close:
        # Use today's expiry if available
        # ---------------------------------------------

        if now.time() < market_close:

            for expiry in expiries:

                if expiry >= today:

                    chosen = expiry

                    break

        # ---------------------------------------------
        # After market close:
        # Skip today's expiry
        # ---------------------------------------------

        else:

            chosen = None

            for expiry in expiries:

                if expiry > today:

                    chosen = expiry

                    break

            if chosen is None:
                chosen = expiries[-1]

        return [

            c

            for c in contracts

            if c.expiry.date() == chosen

        ]


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("EXPIRY SELECTOR READY")

    print("=" * 60)