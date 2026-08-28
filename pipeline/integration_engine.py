"""
=========================================================
QUANT ULTRA
Integration Engine
=========================================================
Central orchestration layer for the trading pipeline.
All shared services are supplied by Runtime.
=========================================================
"""

from core.execution_router import (
    ExecutionRouter,
    ExecutionType,
)

from execution.execution_context import ExecutionContext


TEST_MODE = False


class IntegrationEngine:

    def __init__(
        self,
        config,
        watchlist,
        scanner,
        market,
        guardian,
        cost,
        margin,
        brain,
        decision,
        orders,
        dashboard,
        report,
        router,
        equity_adapter,
        option_pipeline,
    ):

        self.config = config

        self.watchlist = watchlist

        self.scanner = scanner

        self.market = market

        self.guardian = guardian

        self.cost = cost

        self.margin = margin

        self.brain = brain

        self.decision = decision

        self.orders = orders

        self.dashboard = dashboard

        self.report = report

        self.router = router

        self.equity_adapter = equity_adapter

        self.option_pipeline = option_pipeline

    # -------------------------------------------------

    def run(self):

        print()
        print("=" * 80)
        print("🚀 QUANT ULTRA INTEGRATION ENGINE")
        print("=" * 80)

        # -------------------------------------------------
        # Scanner
        # -------------------------------------------------

        analysis = self.scanner.best_trade()

        if analysis is None:

            print(
                "No opportunities found."
            )

            return

        # -------------------------------------------------
        # Guardian AI
        # -------------------------------------------------

        guardian = self.guardian.evaluate()

        # -------------------------------------------------
        # Market Intelligence
        # -------------------------------------------------

        market = self.market.evaluate(

            guardian=guardian,

            vix=None,

            fii=None,

            gift=None,

            global_market=None,

            calendar=None,
        )

        market["reasons"] = (

            analysis.reasons

            + guardian.get(
                "reasons",
                [],
            )
        )

        # Enrich the canonical analysis object before
        # it reaches the Trading Brain.

        analysis.market_score = (
            market["market_score"]
        )

        analysis.metadata["market_bias"] = (
            market["market_bias"]
        )

        # -------------------------------------------------
        # Capital / Risk
        # -------------------------------------------------

        capital = self.config.get(
            "capital",
            10000,
        )

        risk_percent = self.config.get(
            "risk_percent",
            1,
        )

        # =================================================
        # EXECUTION ROUTER
        # =================================================

        execution = self.router.decide(

            capital=capital,

            technical_score=(
                analysis.technical_score
            ),
        )

        print()
        print("=" * 60)
        print("⚙ EXECUTION MODE")
        print("=" * 60)

        print(
            execution.value
        )

        print("=" * 60)

        # =================================================
        # CREATE TRADE PLAN
        # =================================================

        candidate = None

        if execution == ExecutionType.EQUITY:

            trade = (
                self.equity_adapter.create_trade(

                    analysis,

                    capital,

                    risk_percent,
                )
            )

            selected_symbol = trade.symbol

        else:

            trade, candidate = (
                self.option_pipeline.execute(

                    analysis=analysis,

                    capital=capital,

                    risk_percent=risk_percent,
                )
            )

            selected_symbol = (
                candidate.contract.trading_symbol
            )

        trade.confidence = (
            analysis.confidence
        )

        trade.technical_score = (
            analysis.technical_score
        )

        trade.market_score = (
            analysis.market_score
        )

        # -------------------------------------------------
        # Option Contract Metadata
        # -------------------------------------------------

        if candidate is not None:

            trade.instrument_key = (
                candidate.contract.instrument_key
            )

            trade.trading_symbol = (
                candidate.contract.trading_symbol
            )

            trade.underlying = (
                candidate.contract.underlying
            )

            trade.exchange = (
                candidate.contract.exchange
            )

            trade.expiry = (
                candidate.contract.expiry
            )

            trade.strike = (
                candidate.contract.strike
            )

            trade.option_type = (
                candidate.contract.option_type
            )

            trade.lot_size = (
                candidate.contract.lot_size
            )

        # -------------------------------------------------
        # Cost Engine
        # -------------------------------------------------

        cost = self.cost.calculate(

            trade.entry,

            trade.target,

            trade.quantity,
        )

        trade.apply_cost_report(
            cost,
        )

        print()
        print("=" * 60)
        print("💸 COST REPORT")
        print("=" * 60)

        for key, value in cost.items():

            print(
                f"{key:18}: {value}"
            )

        print("=" * 60)

        # -------------------------------------------------
        # Margin Engine
        # -------------------------------------------------

        margin = self.margin.calculate(

            available_margin=capital,

            required_margin=(
                trade.capital_used * 0.20
            ),
        )

        # -------------------------------------------------
        # Execution Context
        # -------------------------------------------------

        context = ExecutionContext(

            market_open=True,

            trading_allowed=True,

            broker_connected=True,

            margin_available=getattr(
                margin,
                "approved",
                True,
            ),

            good_liquidity=True,

            spread_ok=True,

            duplicate_position=False,
        )

        # =================================================
        # Trading Brain
        # =================================================

        print()
        print("=" * 60)
        print("🧠 TRADING BRAIN")
        print("=" * 60)

        brain_result = self.brain.evaluate(

            analysis,

            trade,

            cost,

            context,
        )

        fusion = None

        report = None

        if brain_result.get(
            "success",
            False,
        ):

            fusion = brain_result.get(
                "fusion",
            )

            report = brain_result.get(
                "report",
            )

            print(
                "✅ Trading Brain Completed"
            )

        else:

            print()
            print("=" * 60)
            print("❌ Trading Brain Failed")
            print("=" * 60)

            print(
                brain_result.get(
                    "error",
                    "Unknown Error",
                )
            )

            return

        # -------------------------------------------------
        # Decision Engine
        # -------------------------------------------------

        decision = self.decision.from_fusion(

            analysis,

            trade,

            fusion,

            margin,
        )

        # -------------------------------------------------
        # Dashboard
        # -------------------------------------------------

        self.dashboard.display(

            account={

                "broker": "UPSTOX",

                "cash": capital,

                "margin": capital,

                "buying_power": capital * 5,
            },

            analysis=analysis,

            intelligence=market,

            decision=decision,

            portfolio={

                "positions": 0,

                "capital_used": 0,

                "risk": 0,
            },
        )

        # =================================================
        # Order Execution
        # =================================================

        approved = decision["Approved"]

        if TEST_MODE:

            print()
            print("=" * 60)
            print("🧪 TEST MODE ENABLED")
            print("=" * 60)
            print("Execution bypass is active.")
            print("=" * 60)

            approved = True

        if approved:

            print()
            print("=" * 60)
            print("🚀 ORDER EXECUTION")
            print("=" * 60)

            print()
            print("=" * 60)
            print("DEBUG")
            print("=" * 60)

            print(
                "trade.side              :",
                trade.side,
            )

            print(
                "trade.symbol            :",
                trade.symbol,
            )

            print(
                "decision recommendation :",
                decision["Recommendation"],
            )

            print(
                "decision approved       :",
                decision["Approved"],
            )

            print("=" * 60)

            self.orders.place_order(

                symbol=selected_symbol,

                side=trade.side,

                entry=trade.entry,

                stop_loss=trade.stop_loss,

                target=trade.target,

                quantity=trade.quantity,

                mode=self.config.profile(),
            )

        else:

            print()
            print("=" * 60)
            print("🚫 TRADE BLOCKED")
            print("=" * 60)

            print(
                f"Recommendation : "
                f"{decision['Recommendation']}"
            )

            print(
                f"Approved       : "
                f"{decision['Approved']}"
            )

            print("=" * 60)

        # -------------------------------------------------
        # End of Pipeline
        # -------------------------------------------------

        print()
        print("=" * 80)
        print("✅ PIPELINE COMPLETED")
        print("=" * 80)


# =========================================================
# Standalone Runtime Entry
# =========================================================

if __name__ == "__main__":

    from runtime.runtime import Runtime

    runtime = Runtime()

    runtime.initialize()

    runtime.get(
        "integration_engine",
    ).run()
