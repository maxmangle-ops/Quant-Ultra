"""
=========================================================
QUANT ULTRA
WebSocket Manager
=========================================================
"""

import os
from dotenv import load_dotenv

import upstox_client

load_dotenv()


class WebSocketManager:

    def __init__(self):

        configuration = upstox_client.Configuration()

        configuration.access_token = os.getenv(
            "UPSTOX_ACCESS_TOKEN"
        )

        self.api_client = upstox_client.ApiClient(
            configuration
        )

        self.streamer = None

    # -------------------------------------------------

    def connect(

        self,

        instrument_keys,

        on_tick,

    ):

        self.streamer = upstox_client.MarketDataStreamerV3(

            self.api_client,

            instrument_keys,

            "full",

        )

        # -----------------------------------------

        self.streamer.on("open", self.on_open)

        self.streamer.on("message", on_tick)

        self.streamer.on("close", self.on_close)

        self.streamer.on("error", self.on_error)

        # -----------------------------------------

        self.streamer.connect()

    # -------------------------------------------------

    def on_open(self):

        print()

        print("=" * 60)

        print("🟢 WEBSOCKET CONNECTED")

        print("=" * 60)

    # -------------------------------------------------

    def on_close(self):

        print()

        print("🔴 WebSocket Closed")

    # -------------------------------------------------

    def on_error(self, error):

        print()

        print("❌ WebSocket Error")

        print(error)

    # -------------------------------------------------

    def disconnect(self):

        if self.streamer:

            self.streamer.disconnect()


# ---------------------------------------------------------

if __name__ == "__main__":

    manager = WebSocketManager()

    def on_tick(message):

        print(message)

    manager.connect(

        [

            "NSE_EQ|INE009A01021"

        ],

        on_tick,

    )