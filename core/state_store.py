"""
=========================================================
QUANT ULTRA
State Store
=========================================================
Central application state for Quant Ultra.
=========================================================
"""

from copy import deepcopy


class StateStore:

    def __init__(self):

        self.reset()

    # =====================================================
    # Reset
    # =====================================================

    def reset(self):

        self._state = {

            "runtime": {},

            "market": {},

            "analysis": {},

            "trade_plan": None,

            "orders": [],

            "positions": [],

            "portfolio": {},

            "account": {},

            "reports": {},

            "statistics": {},

            "metadata": {},

        }

    # =====================================================
    # Generic
    # =====================================================

    def set(

        self,

        key,

        value,

    ):

        self._state[key] = value

    # -----------------------------------------------------

    def get(

        self,

        key,

        default=None,

    ):

        return self._state.get(

            key,

            default,

        )

    # -----------------------------------------------------

    def update(

        self,

        key,

        value,

    ):

        if (

            key not in self._state

            or

            not isinstance(

                self._state[key],

                dict,

            )

        ):

            self._state[key] = {}

        self._state[key].update(value)

    # =====================================================
    # Orders
    # =====================================================

    def add_order(

        self,

        order,

    ):

        self._state["orders"].append(order)

    # =====================================================
    # Positions
    # =====================================================

    def add_position(

        self,

        position,

    ):

        self._state["positions"].append(position)

    # =====================================================
    # Snapshot
    # =====================================================

    def snapshot(self):

        return deepcopy(

            self._state

        )

    # =====================================================
    # Clear
    # =====================================================

    def clear_orders(self):

        self._state["orders"].clear()

    # -----------------------------------------------------

    def clear_positions(self):

        self._state["positions"].clear()

    # =====================================================

    def __contains__(

        self,

        key,

    ):

        return key in self._state

    # =====================================================

    def __getitem__(

        self,

        key,

    ):

        return self._state[key]

    # =====================================================

    def __setitem__(

        self,

        key,

        value,

    ):

        self._state[key] = value


# ---------------------------------------------------------

if __name__ == "__main__":

    store = StateStore()

    store.set(

        "market",

        {

            "symbol": "NIFTY",

            "price": 24250,

        },

    )

    print()

    print("=" * 60)

    print("STATE STORE READY")

    print("=" * 60)

    print()

    print(store.snapshot())