"""
=========================================================
QUANT ULTRA
Market Scheduler
=========================================================
"""

import time
from datetime import datetime

from pipeline.engine import Pipeline


class MarketScheduler:

    def __init__(self):

        self.pipeline = Pipeline()

        self.running = False

        self.market_start = (9, 20)

        self.last_run = None

    # -------------------------------------------------

    def market_open(self):

        now = datetime.now()

        return (

            now.hour > self.market_start[0]

            or

            (

                now.hour == self.market_start[0]

                and

                now.minute >= self.market_start[1]

            )

        )

    # -------------------------------------------------

    def execute(self):

        print()

        print("=" * 60)

        print("🚀 QUANT ULTRA SCHEDULER")

        print("=" * 60)

        self.running = True

        while self.running:

            now = datetime.now()

            # Wait for Market

            if not self.market_open():

                print(

                    f"[{now.strftime('%H:%M:%S')}] Waiting for market..."

                )

                time.sleep(30)

                continue

            # Execute once every minute

            minute = now.strftime("%Y%m%d%H%M")

            if minute != self.last_run:

                print()

                print(

                    f"📊 Running Pipeline : {now.strftime('%H:%M')}"

                )

                self.pipeline.run()

                self.last_run = minute

            time.sleep(1)

    # -------------------------------------------------

    def stop(self):

        self.running = False

        print()

        print("🛑 Scheduler Stopped")


# ---------------------------------------------------------

if __name__ == "__main__":

    scheduler = MarketScheduler()

    scheduler.execute()