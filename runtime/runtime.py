"""
=========================================================
QUANT ULTRA
Runtime
Version : 2.3
Status  : Runtime Kernel
=========================================================
Initializes and wires the complete Quant Ultra platform.
=========================================================
"""

from core.service_container import ServiceContainer

# =========================================================
# Core
# =========================================================

from config.config_manager import ConfigManager

# Future Runtime Service
from core.instrument_manager import InstrumentManager

# =========================================================
# Trading
# =========================================================

from watchlist.watchlist_manager import WatchlistManager
from position.position_manager import PositionManager
from position.trade_manager import TradeManager

from paper.paper_trader import PaperTrader
from orders.order_manager import OrderManager

# =========================================================
# Monitoring
# =========================================================

from exit.exit_manager import ExitManager
from monitor.trade_monitor import TradeMonitor

# =========================================================
# Pipeline
# =========================================================

from pipeline.integration_engine import IntegrationEngine

# =========================================================
# Dashboard
# =========================================================

from dashboard.dashboard import Dashboard
from reports.report_generator import ReportGenerator


class Runtime:

    def __init__(self):

        self.container = ServiceContainer()

        self.initialized = False
        self.running = False

    # =====================================================
    # Initialize Runtime
    # =====================================================

    def initialize(self):

        if self.initialized:
            return

        print()
        print("=" * 70)
        print("🚀 INITIALIZING QUANT ULTRA")
        print("=" * 70)

        self.register_core()
        self.register_trading()
        self.register_services()

        self.initialized = True

        print()
        print("=" * 70)
        print("✅ RUNTIME READY")
        print("=" * 70)

    # =====================================================
    # Core
    # =====================================================

    def register_core(self):

        config = ConfigManager()

        self.container.register(
            "config",
            config,
        )

    # =====================================================
    # Trading
    # =====================================================

    def register_trading(self):

        watchlist = WatchlistManager()

        instrument_manager = InstrumentManager()

        position_manager = PositionManager()

        trade_manager = TradeManager()

        paper_trader = PaperTrader(position_manager)

        order_manager = OrderManager(paper_trader)

        exit_manager = ExitManager()

        trade_monitor = TradeMonitor(
            position_manager=position_manager,
            exit_manager=exit_manager,
        )

        dashboard = Dashboard()

        report_generator = ReportGenerator()

        integration_engine = IntegrationEngine(

            config=self.get("config"),

            watchlist=watchlist,

            orders=order_manager,

            dashboard=dashboard,

            report=report_generator,

        )

        # -------------------------------------------------

        self.container.register(
            "watchlist",
            watchlist,
        )

        self.container.register(
            "instrument_manager",
            instrument_manager,
        )


        self.container.register(
            "position_manager",
            position_manager,
        )

        self.container.register(
            "trade_manager",
            trade_manager,
        )

        self.container.register(
            "paper_trader",
            paper_trader,
        )

        self.container.register(
            "order_manager",
            order_manager,
        )

        self.container.register(
            "exit_manager",
            exit_manager,
        )

        self.container.register(
            "trade_monitor",
            trade_monitor,
        )

        self.container.register(
            "dashboard",
            dashboard,
        )

        self.container.register(
            "report_generator",
            report_generator,
        )

        self.container.register(
            "integration_engine",
            integration_engine,
        )

    # =====================================================
    # Runtime Services
    # =====================================================

    def register_services(self):

        # Import here to avoid circular imports

        from engine.trading_loop import TradingLoop
        from market.websocket_stream import WebSocketService

        # ---------------------------------------------
        # Trading Loop
        # ---------------------------------------------

        trading_loop = TradingLoop(

            integration_engine=self.get("integration_engine"),

            position_manager=self.get("position_manager"),

        )

        # ---------------------------------------------
        # Build Subscription List
        # ---------------------------------------------

        instrument_keys = []

        watchlist = self.get("watchlist")
        instrument_manager = self.get("instrument_manager")

        for symbol in watchlist.get_symbols():

            instrument = instrument_manager.get(symbol)

            if instrument is not None:

                instrument_keys.append(instrument.instrument_key)

        # Fallback only when watchlist is empty
        if not instrument_keys:
            instrument_keys = None

        print("\n===== WATCHLIST =====")
        print(watchlist.get_symbols())

        print("\n===== INSTRUMENT KEYS =====")
        print(instrument_keys)

        # ---------------------------------------------
        # WebSocket Service
        # ---------------------------------------------

        websocket = WebSocketService(

            trade_monitor=self.get("trade_monitor"),

            integration_engine=self.get("integration_engine"),

            instrument_manager=instrument_manager,

            instruments=instrument_keys,

        )

        # ---------------------------------------------
        # Register Services
        # ---------------------------------------------

        self.container.register(

            "trading_loop",

            trading_loop,

        )

        self.container.register(

            "websocket",

            websocket,

        )

    # =====================================================

    def start(self):

        if self.running:
            return

        self.running = True

        print()
        print("=" * 70)
        print("🚀 QUANT ULTRA STARTED")
        print("=" * 70)

        # ---------------------------------------------
        # Start Runtime Services
        # ---------------------------------------------

        self.get("trading_loop").start()

        self.get("websocket").start()

    # =====================================================

    def stop(self):

        if not self.running:
            return

        self.running = False

        if self.exists("websocket"):

            self.get("websocket").stop()

        if self.exists("trading_loop"):

            self.get("trading_loop").stop()

        print()
        print("=" * 70)
        print("🛑 QUANT ULTRA STOPPED")
        print("=" * 70)

    # =====================================================

    def get(self, name):

        return self.container.get(name)

    # =====================================================

    def exists(self, name):

        return self.container.exists(name)

    # =====================================================

    def list_services(self):

        return self.container.list_services()


# =========================================================

if __name__ == "__main__":

    runtime = Runtime()

    runtime.initialize()

    runtime.start()

    print()

    print("Registered Services")

    print("-" * 40)

    for service in runtime.list_services():

        print(service)

    try:

        while True:
            pass

    except KeyboardInterrupt:

        runtime.stop()