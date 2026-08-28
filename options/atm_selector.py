"""
=========================================================
QUANT ULTRA
ATM Strike Selector
=========================================================
Selects the nearest ATM strike.
=========================================================
"""


class ATMSelector:

    def __init__(self):
        pass

    # -------------------------------------------------

    def nearest_strike(

        self,

        spot_price,

        step,

    ):

        return round(

            spot_price / step

        ) * step


# ---------------------------------------------------------

if __name__ == "__main__":

    selector = ATMSelector()

    print()

    print("=" * 60)

    print("ATM SELECTOR")

    print("=" * 60)

    prices = [

        24239,

        24101,

        24988,

        50341,

    ]

    for price in prices:

        strike = selector.nearest_strike(

            spot_price=price,

            step=50,

        )

        print(

            f"{price} -> {strike}"

        )