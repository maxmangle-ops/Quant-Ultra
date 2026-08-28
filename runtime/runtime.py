"""
=========================================================
QUANT ULTRA
Runtime
Version : 3.0
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
from core.instrument_manager import InstrumentManager
from core.execution_router import ExecutionRouter

# =========================================================
# Trading
# =========================================================

from watchlist.watchlist_manager import WatchlistManager
from position.position_manager import PositionManager
from position.trade_manager import TradeManager

from paper.paper_trader import (
    PaperTrader,
    configure_paper_trader,
)

from orders.order_manager import OrderManager

# =========================================================
# Monitoring
# =========================================================

from exit.exit_manager import ExitManager
from monitor.trade_monitor import TradeMonitor

# =========================================================
# Scanner
# =========================================================

from scanner.multi_symbol_scanner import MultiSymbolScanner

# =========================================================
# Intelligence / Market
# =========================================================

from market.market_intelligence import MarketIntelligence
from guardian.news_guardian import NewsGuardian
from intelligence.brain import TradingBrain

# =========================================================
# Cost / Margin
# =========================================================

from cost.charges import CostEngine
from margin.calculator import MarginEngine

# =========================================================
# Decision
# =========================================================

from decision.engine import DecisionEngine

# =========================================================
# Execution
# =========================================================

from execution.equity_adapter import EquityAdapter
from execution.option_pipeline import OptionPipeline

# =========================================================
# Pipeline
# =========================================================

from pipeline.integration_engine import IntegrationEngine

# =========================================================
# Dashboard / Reports
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
    # Core Services
    # =====================================================

    def register_core(self):

        config = ConfigManager()

        instrument_manager = InstrumentManager()

        self.container.register(
            "config",
            config,
        )

        self.container.register(
            "instrument_manager",
            instrument_manager,
        )

    # =====================================================
    # Trading Services
    # =====================================================

    def register_trading(self):

        watchlist = WatchlistManager()

        trade_manager = TradeManager()

        position_manager = PositionManager(
            trade_manager=trade_manager,
        )

        paper_trader = PaperTrader(
            position_manager=position_manager,
        )

        # Configure the compatibility API to point at the
        # Runtime-owned PaperTrader instead of creating
        # another trading engine at import time.
        configure_paper_trader(
            paper_trader,
        )

        order_manager = OrderManager(
            paper_trader=paper_trader,
        )

        exit_manager = ExitManager()

        trade_monitor = TradeMonitor(
            position_manager=position_manager,
            exit_manager=exit_manager,
        )

        dashboard = Dashboard()

        report_generator = ReportGenerator()

        # -------------------------------------------------
        # Market / Intelligence
        # -------------------------------------------------

        market = MarketIntelligence()

        guardian = NewsGuardian()

        brain = TradingBrain()

        # -------------------------------------------------
        # Risk / Cost
        # -------------------------------------------------

        cost = CostEngine()

        margin = MarginEngine()

        # -------------------------------------------------
        # Decision
        # -------------------------------------------------

        decision = DecisionEngine()

        # -------------------------------------------------
        # Execution
        # -------------------------------------------------

        router = ExecutionRouter()

        equity_adapter = EquityAdapter()

        option_pipeline = OptionPipeline()

        # -------------------------------------------------
        # Scanner
        # -------------------------------------------------

        scanner = MultiSymbolScanner(
            watchlist.get_symbols(),
        )

        # -------------------------------------------------
        # Integration Engine
        # -------------------------------------------------

        integration_engine = IntegrationEngine(

            config=config,

            watchlist=watchlist,

            scanner=scanner,

            market=market,

            guardian=guardian,

            cost=cost,

            margin=margin,

            brain=brain,

            decision=decision,

            orders=order_manager,

            dashboard=dashboard,

            report=report_generator,

            router=router,

            equity_adapter=equity_adapter,

            option_pipeline=option_pipeline,
        )

        # -------------------------------------------------
        # Register Core Trading Services
        # -------------------------------------------------

        self.container.register(
            "watchlist",
            watchlist,
        )

        self.container.register(
            "trade_manager",
            trade_manager,
        )

        self.container.register(
            "position_manager",
            position_manager,
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

        # -------------------------------------------------
        # Register Intelligence / Risk Services
        # -------------------------------------------------

        self.container.register(
            "market_intelligence",
            market,
        )

        self.container.register(
            "news_guardian",
            guardian,
        )

        self.container.register(
            "trading_brain",
            brain,
        )

        self.container.register(
            "cost_engine",
            cost,
        )

        self.container.register(
            "margin_engine",
            margin,
        )

        self.container.register(
            "decision_engine",
            decision,
        )

        # -------------------------------------------------
        # Register Execution Services
        # -------------------------------------------------

        self.container.register(
            "execution_router",
            router,
        )

        self.container.register(
            "equity_adapter",
            equity_adapter,
        )

        self.container.register(
            "option_pipeline",
            option_pipeline,
        )

        # -------------------------------------------------
        # Register Scanner
        # -------------------------------------------------

        self.container.register(
            "scanner",
            scanner,
        )

        # -------------------------------------------------
        # Register Pipeline
        # -------------------------------------------------

        self.container.register(
            "integration_engine",
            integration_engine,
        )

    # =====================================================
    # Runtime Services
    # =====================================================

    def register_services(self):

        # Local imports keep the runtime composition root
        # independent from the service implementations.
        from engine.trading_loop import TradingLoop
        from market.websocket_stream import WebSocketService

        # -------------------------------------------------
        # Trading Loop
        # -------------------------------------------------

        trading_loop = TradingLoop(

            integration_engine=self.get(
                "integration_engine",
            ),

            position_manager=self.get(
                "position_manager",
            ),
        )

        # -------------------------------------------------
        # Build Subscription List
        # -------------------------------------------------

        instrument_keys = []

        watchlist = self.get(
            "watchlist",
        )

        instrument_manager = self.get(
            "instrument_manager",
        )

        for symbol in watchlist.get_symbols():

            instrument = instrument_manager.get(
                symbol,
            )

            if instrument is not None:

                instrument_keys.append(
                    instrument.instrument_key,
                )

        # Keep the WebSocket fallback behavior when the
        # watchlist does not resolve to any instruments.
        if not instrument_keys:
            instrument_keys = None

        print()
        print("===== WATCHLIST =====")
        print(watchlist.get_symbols())

        print()
        print("===== INSTRUMENT KEYS =====")
        print(instrument_keys)

        # -------------------------------------------------
        # WebSocket Service
        # -------------------------------------------------

        websocket = WebSocketService(

            trade_monitor=self.get(
                "trade_monitor",
            ),

            integration_engine=self.get(
                "integration_engine",
            ),

            instrument_manager=instrument_manager,

            instruments=instrument_keys,
        )

        # -------------------------------------------------
        # Register Runtime Services
        # -------------------------------------------------

        self.container.register(
            "trading_loop",
            trading_loop,
        )

        self.container.register(
            "websocket",
            websocket,
        )

    # =====================================================
    # Start
    # =====================================================

    def start(self):

        if not self.initialized:
            self.initialize()

        if self.running:
            return

        self.running = True

        print()
        print("=" * 70)
        print("🚀 QUANT ULTRA STARTED")
        print("=" * 70)

        # -------------------------------------------------
        # Start Runtime Services
        # -------------------------------------------------

        self.get(
            "trading_loop",
        ).start()

        self.get(
            "websocket",
        ).start()

    # =====================================================
    # Stop
    # =====================================================

    def stop(self):

        if not self.running:
            return

        self.running = False

        if self.exists("websocket"):

            self.get(
                "websocket",
            ).stop()

        if self.exists("trading_loop"):

            self.get(
                "trading_loop",
            ).stop()

        print()
        print("=" * 70)
        print("🛑 QUANT ULTRA STOPPED")
        print("=" * 70)

    # =====================================================
    # Service Access
    # =====================================================

    def get(self, name):

        return self.container.get(
            name,
        )

    # =====================================================

    def exists(self, name):

        return self.container.exists(
            name,
        )

    # =====================================================

    def list_services(self):

        return self.container.list_services()


# =========================================================
# Standalone Runtime Test
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

            import time

            time.sleep(1)

    except KeyboardInterrupt:

        runtime.stop()
