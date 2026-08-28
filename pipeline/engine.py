"""
=========================================================
QUANT ULTRA
Trading Pipeline
=========================================================
"""

from engine.live_analyzer import analyze

from market.market_intelligence import MarketIntelligence

from risk.risk_manager import calculate_position

from cost.charges import CostEngine

from margin.calculator import MarginEngine

from decision.engine import DecisionEngine

from orders.order_manager import OrderManager

from account.account_manager import AccountManager

from scanner.multi_symbol_scanner import MultiSymbolScanner

from watchlist.watchlist_manager import WatchlistManager


class Pipeline:

    def __init__(self):

        self.cost_engine = CostEngine()

        self.margin_engine = MarginEngine()

        self.decision_engine = DecisionEngine()

        self.order_manager = OrderManager()

        self.market_engine = MarketIntelligence()

        self.account_manager = AccountManager()

        self.watchlist = WatchlistManager()

    # -------------------------------------------------

    def run(self):

        print()

        print("=" * 60)

        print("🚀 QUANT ULTRA PIPELINE")

        print("=" * 60)

        # ---------------------------------------------
        # Scanner
        # ---------------------------------------------

        symbols = self.watchlist.get_symbols()

        scanner = MultiSymbolScanner(symbols)

        analysis = scanner.best_trade()

        if analysis is None:

            print("No symbol available.")

            return

        # ---------------------------------------------
        # Market Intelligence
        # ---------------------------------------------

        intelligence = self.market_engine.evaluate(

            guardian={

                "guardian_score": analysis.get(

                    "guardian_score",

                    50,

                ),

                "reasons": analysis.get(

                    "reasons",

                    [],

                ),

            },

            vix=None,

            fii=None,

            gift=None,

            global_market=None,

            calendar=None,

        )

        print()

        print("Market Score :", intelligence["market_score"])

        print("Market Bias  :", intelligence["market_bias"])

        # ---------------------------------------------
        # WAIT
        # ---------------------------------------------

        if analysis["technical_score"] < 60:

            print()

            print("WAIT")

            return

        # ---------------------------------------------
        # Risk
        # ---------------------------------------------

        trade = calculate_position(

            entry_price=analysis["price"],

            atr=analysis["atr"],

            capital=10000,

            risk_percent=1,

        )

        # ---------------------------------------------
        # Cost
        # ---------------------------------------------

        cost = self.cost_engine.calculate(

            trade["Entry"],

            trade["Target"],

            trade["Quantity"],

        )

        # ---------------------------------------------
        # Margin
        # ---------------------------------------------

        margin = self.margin_engine.calculate(

            available_margin=10000,

            required_margin=trade["Entry"]

            * trade["Quantity"]

            * 0.20,

        )

        # ---------------------------------------------
        # Decision
        # ---------------------------------------------

        decision = self.decision_engine.calculate(

            analysis,

            trade,

            cost,

            margin,

        )

        print()

        print("=" * 60)

        print("FINAL DECISION")

        print("=" * 60)

        print(decision)

        # ---------------------------------------------
        # Execute
        # ---------------------------------------------

        if decision["Approved"]:

            self.order_manager.place_order(

                symbol=analysis["symbol"],

                side=analysis["signal"],

                entry=trade["Entry"],

                stop_loss=trade["StopLoss"],

                target=trade["Target"],

                quantity=trade["Quantity"],

                mode="PAPER",

            )

        else:

            print()

            print("Trade Rejected")