"""
=========================================================
QUANT ULTRA
Order Manager
Version : 2.0
Status  : Runtime Ready
=========================================================
Handles Paper + Live Orders
=========================================================
"""

from datetime import datetime

from paper.paper_trader import PaperTrader
from models.trade_models import TradePlan


class OrderManager:

    def __init__(self, paper_trader=None):
        """
        Order Manager

        Parameters
        ----------
        paper_trader : PaperTrader | None

        Runtime will inject the shared PaperTrader.
        During migration a local instance is created.
        """

        self.orders = []

        # ---------------------------------------------
        # Dependency Injection (Runtime Ready)
        # ---------------------------------------------

        if paper_trader is None:
            paper_trader = PaperTrader()

        self.paper_trader = paper_trader

    # -------------------------------------------------
    # Place Order
    # -------------------------------------------------

    def place_order(
        self,
        symbol=None,
        side=None,
        entry=None,
        stop_loss=None,
        target=None,
        quantity=None,
        mode="PAPER",
    ):

        trade_plan = symbol if isinstance(symbol, TradePlan) else None

        if trade_plan is not None:
            symbol = trade_plan.symbol
            side = trade_plan.side
            entry = trade_plan.entry
            stop_loss = trade_plan.stop_loss
            target = trade_plan.target
            quantity = trade_plan.quantity

        order = {
            "order_id": len(self.orders) + 1,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "symbol": symbol,
            "side": side,
            "entry": entry,
            "stop_loss": stop_loss,
            "target": target,
            "quantity": quantity,
            "mode": mode,
            "status": "PLACED",
        }

        self.orders.append(order)

        print()
        print("=" * 60)
        print("📝 ORDER PLACED")
        print("=" * 60)

        for k, v in order.items():
            print(f"{k:15}: {v}")

        print("=" * 60)

        # ---------------------------------------------
        # Execute Order
        # ---------------------------------------------

        if mode.upper() == "PAPER":

            self.paper_trader.open_trade(
                symbol=symbol,
                side=side,
                entry=entry,
                stop_loss=stop_loss,
                target=target,
                quantity=quantity,
            )

        else:

            print()
            print("⚠ LIVE ORDER EXECUTION COMING SOON")

        return order

    # -------------------------------------------------
    # Cancel
    # -------------------------------------------------

    def cancel_order(self, order_id):

        for order in self.orders:

            if order["order_id"] == order_id:

                order["status"] = "CANCELLED"

                print(f"✅ Order {order_id} Cancelled")

                return order

        print("❌ Order Not Found")

        return None

    # -------------------------------------------------
    # Modify
    # -------------------------------------------------

    def modify_order(
        self,
        order_id,
        stop_loss=None,
        target=None,
    ):

        for order in self.orders:

            if order["order_id"] == order_id:

                if stop_loss is not None:
                    order["stop_loss"] = stop_loss

                if target is not None:
                    order["target"] = target

                print(f"✅ Order {order_id} Modified")

                return order

        print("❌ Order Not Found")

        return None

    # -------------------------------------------------
    # Status
    # -------------------------------------------------

    def get_orders(self):

        return self.orders

    # -------------------------------------------------

    def get_paper_trader(self):

        return self.paper_trader


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    manager = OrderManager()

    manager.place_order(
        symbol="NIFTY",
        side="BUY",
        entry=25000,
        stop_loss=24950,
        target=25100,
        quantity=1,
        mode="PAPER",
    )