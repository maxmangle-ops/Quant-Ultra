"""
=========================================================
QUANT ULTRA
Trade Monitor
Version : 2.0
Status  : Runtime Ready
=========================================================
Monitors all open trades continuously.
=========================================================
"""

import time

from exit.exit_manager import ExitManager


class TradeMonitor:

    def __init__(
        self,
        position_manager,
        exit_manager=None,
    ):
        """
        Trade Monitor

        Parameters
        ----------
        position_manager : PositionManager

        exit_manager : ExitManager | None

        Runtime will inject the shared ExitManager.
        During migration a local instance is created.
        """

        self.position_manager = position_manager

        # ---------------------------------------------
        # Dependency Injection (Runtime Ready)
        # ---------------------------------------------

        if exit_manager is None:
            exit_manager = ExitManager()

        self.exit_manager = exit_manager

        self.running = False

    # -----------------------------------------------------

    def process_price(self, symbol, ltp):

        self.position_manager.update_price(symbol, ltp)

        positions = self.position_manager.get_open_positions()

        for position in positions:

            if position["symbol"] != symbol:
                continue

            result = self.exit_manager.evaluate(
                position,
                ltp,
            )

            if result["exit"]:

                self.position_manager.close_position(
                    position["position_id"],
                    result["reason"],
                )

                print()

                print("=" * 60)
                print("🚨 TRADE EXITED")
                print("=" * 60)

                print(f"Symbol     : {symbol}")
                print(f"Reason     : {result['reason']}")
                print(f"Exit Price : ₹{result['exit_price']}")
                print(f"PnL        : ₹{result['pnl']}")

                print("=" * 60)

    # -----------------------------------------------------
    # Compatibility Mode
    # (Will disappear once WebSocket becomes event driven)
    # -----------------------------------------------------

    def run(self, price_callback):
        """
        Compatibility mode.

        Used for testing and simulation.

        Production Runtime will call
        process_price() directly from
        WebSocket events.
        """

        self.running = True

        print()
        print("=" * 60)
        print("📡 TRADE MONITOR STARTED")
        print("=" * 60)

        while self.running:

            tick = price_callback()

            if tick is not None:

                self.process_price(
                    tick["symbol"],
                    tick["ltp"],
                )

            time.sleep(1)

    # -----------------------------------------------------

    def stop(self):

        self.running = False

        print()
        print("🛑 Trade Monitor Stopped")


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    from position.position_manager import PositionManager

    pm = PositionManager()

    pm.open_position(
        symbol="NIFTY",
        side="BUY",
        entry=25000,
        quantity=1,
        stop_loss=24950,
        target=25100,
    )

    prices = [
        25010,
        25025,
        25040,
        25070,
        25095,
        25110,
    ]

    def fake_feed():

        if fake_feed.index >= len(prices):
            return None

        ltp = prices[fake_feed.index]

        fake_feed.index += 1

        return {
            "symbol": "NIFTY",
            "ltp": ltp,
        }

    fake_feed.index = 0

    monitor = TradeMonitor(pm)

    monitor.run(fake_feed)