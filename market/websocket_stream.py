"""
=========================================================
QUANT ULTRA
WebSocket Service
Version : 2.1
Status  : Runtime Ready
=========================================================
Receives live ticks from Upstox and drives the entire
Quant Ultra trading pipeline.
=========================================================
"""

from datetime import datetime
import os

from dotenv import load_dotenv
import upstox_client

from market.candle_builder import update_candle
from market.data_provider import add_candle

load_dotenv()


class WebSocketService:

    def __init__(
        self,
        trade_monitor,
        integration_engine,
        instrument_manager=None,
        instruments=None,
    ):

        self.trade_monitor = trade_monitor

        self.integration_engine = integration_engine
        self.instrument_manager = instrument_manager

        # Runtime injects instrument keys.
        # Fallback only if Runtime provides no subscriptions.
        self.instruments = instruments or [
            "NSE_EQ|INE009A01021"
        ]

        configuration = upstox_client.Configuration()
        configuration.access_token = os.getenv(
            "UPSTOX_ACCESS_TOKEN"
        )

        self.streamer = upstox_client.MarketDataStreamerV3(
            upstox_client.ApiClient(configuration),
            self.instruments,
            "ltpc",
        )

        self._register_events()

    # -------------------------------------------------
    # Event Registration
    # -------------------------------------------------

    def _register_events(self):

        self.streamer.on("open", self.on_open)
        self.streamer.on("message", self.on_message)
        self.streamer.on("error", self.on_error)
        self.streamer.on("close", self.on_close)

    # -------------------------------------------------
    # Future Instrument Manager Hook
    # -------------------------------------------------

    def resolve_symbol(self, instrument_key):

        """
        Temporary resolver.

        Later this will call InstrumentManager.
        """

        if self.instrument_manager is not None:
            for instrument in self.instrument_manager.all():
                if instrument.instrument_key == instrument_key:
                    return instrument.symbol

        # Temporary fallback during migration.
        mapping = {
            "NSE_EQ|INE009A01021": "INFY",
        }
        return mapping.get(instrument_key, instrument_key)

    # -------------------------------------------------

    def start(self):

        print()
        print("=" * 70)
        print("📡 STARTING WEBSOCKET")
        print("=" * 70)

        self.streamer.connect()

    # -------------------------------------------------

    def stop(self):

        try:

            self.streamer.disconnect()

        except Exception:

            pass

    # -------------------------------------------------

    def on_open(self, *args):

        print("🟢 Connected to Upstox WebSocket")

    # -------------------------------------------------

    def on_message(self, message):

        try:

            if "feeds" not in message:

                return

            for instrument_key, feed_data in message["feeds"].items():

                if "ltpc" not in feed_data:

                    continue

                feed = feed_data["ltpc"]

                ltp = float(feed.get("ltp", 0.0))

                qty = int(feed.get("ltq", 0))

                ltt = feed.get("ltt")

                if ltt is not None:
                    tick_time = datetime.fromtimestamp(
                        int(ltt) / 1000
                    )
                else:
                    tick_time = datetime.now()

                symbol = self.resolve_symbol(

                    instrument_key

                )

                print(

                    f"{tick_time.strftime('%H:%M:%S')} | "

                    f"{symbol:<10} | "

                    f"₹{ltp:.2f}"

                )

                # -------------------------------------
                # Position Monitoring
                # -------------------------------------

                self.trade_monitor.process_price(

                    symbol,

                    ltp,

                )

                # -------------------------------------
                # Candle Builder
                # -------------------------------------

                candle = update_candle(
                    
                    symbol,

                    ltp,

                    qty,

                    tick_time,

                )

                if candle:

                    add_candle(candle)

                    print()
                    print("=" * 70)
                    print("🕯 5 MINUTE CANDLE CLOSED")
                    print("=" * 70)

                    print(candle)

                    print()

                    print("🚀 Running Quant Ultra Pipeline...")

                    print()

                    # NOTE:
                    # Pipeline execution remains here until TradingLoop
                    # becomes the event scheduler.
                    self.integration_engine.run()

        except Exception as e:

            print()

            print("=" * 70)

            print("❌ WEBSOCKET ERROR")

            print("=" * 70)

            print(e)

    # -------------------------------------------------

    def on_error(self, error):

        print()

        print("=" * 70)

        print("❌ WEBSOCKET ERROR")

        print("=" * 70)

        print(error)

    # -------------------------------------------------

    def on_close(self, *args):

        print()

        print("🔴 Upstox WebSocket Closed")


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    from runtime.runtime import Runtime

    runtime = Runtime()

    runtime.initialize()

    websocket = runtime.get("websocket")

    websocket.start()