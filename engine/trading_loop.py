"""
=========================================================
QUANT ULTRA
Trading Loop
Version : 3.0
Status  : Runtime Service
=========================================================
"""

import threading
import time


class TradingLoop:

    def __init__(
        self,
        integration_engine,
        position_manager,
        interval=1,
    ):

        self.engine = integration_engine
        self.position_manager = position_manager

        self.interval = interval

        self.running = False

        self.thread = None

    # -------------------------------------------------

    def _run(self):

        print()
        print("=" * 70)
        print("🚀 QUANT ULTRA TRADING LOOP STARTED")
        print("=" * 70)

        while self.running:

            try:

                positions = self.position_manager.get_open_positions()

                if positions:

                    print(
                        f"📍 Monitoring {len(positions)} Open Position(s)"
                    )

                #
                # Scanner / Strategy execution
                # will be Scheduler driven.
                #

            except Exception as e:

                print()
                print("=" * 70)
                print("❌ Trading Loop Error")
                print("=" * 70)
                print(e)

            time.sleep(self.interval)

        print()
        print("🛑 Trading Loop Exited")

    # -------------------------------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._run,
            daemon=True,
            name="TradingLoop",
        )

        self.thread.start()

    # -------------------------------------------------

    def stop(self):

        self.running = False

        if self.thread:

            self.thread.join(timeout=5)

        print()

        print("🛑 Trading Loop Stopped")


# ---------------------------------------------------------

if __name__ == "__main__":

    from runtime.runtime import Runtime

    runtime = Runtime()

    runtime.initialize()

    loop = runtime.get("trading_loop")

    loop.start()

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        loop.stop()