"""
=========================================================
QUANT ULTRA
Trading Brain
=========================================================
Master intelligence orchestrator.
=========================================================
"""

from intelligence.gate_models import GateBundle

from intelligence.gates.technical_gate import TechnicalGate
from intelligence.gates.market_gate import MarketGate
from intelligence.gates.risk_gate import RiskGate
from intelligence.gates.cost_gate import CostGate
from intelligence.gates.execution_gate import ExecutionGate

from intelligence.fusion_engine import FusionEngine
from intelligence.decision_report import DecisionReport


class TradingBrain:

    def __init__(self):

        self.technical_gate = TechnicalGate()
        self.market_gate = MarketGate()
        self.risk_gate = RiskGate()
        self.cost_gate = CostGate()
        self.execution_gate = ExecutionGate()

        self.fusion_engine = FusionEngine()
        self.report_engine = DecisionReport()

    # -------------------------------------------------

    def _build_gate_bundle(

        self,
        analysis,
        trade_plan,
        cost_report,
        execution_context,

    ):

        bundle = GateBundle()

        bundle.add(self.technical_gate.evaluate(analysis))
        bundle.add(self.market_gate.evaluate(analysis))
        bundle.add(self.risk_gate.evaluate(trade_plan))
        bundle.add(self.cost_gate.evaluate(cost_report))
        bundle.add(
            self.execution_gate.evaluate(
                trade_plan,
                execution_context,
            )
        )

        return bundle

    # -------------------------------------------------

    def evaluate(

        self,

        analysis,

        trade_plan,

        cost_report,

        execution_context,

    ):

        print()
        print("=" * 70)
        print("🧠 TRADING BRAIN STARTED")
        print("=" * 70)

        try:

            print("✅ Building Gate Bundle...")

            bundle = self._build_gate_bundle(
                analysis,
                trade_plan,
                cost_report,
                execution_context,
            )

            gate_count = len(getattr(bundle, "gates", []))
            print(f"✅ Gates Executed : {gate_count}")

            print("✅ Running Fusion Engine...")

            fusion = self.fusion_engine.evaluate(bundle)

            print("✅ Fusion Complete")
            print(f"Fusion Score      : {getattr(fusion, 'score', 'N/A')}")
            print(f"Fusion Confidence : {getattr(fusion, 'confidence', 'N/A')}")
            print(f"Fusion Approved   : {getattr(fusion, 'approved', 'N/A')}")

            print("✅ Building Decision Report...")

            report = self.report_engine.generate(fusion)

            print("✅ Trading Brain Finished Successfully")
            print("=" * 70)
            print()

            return {
                "success": True,
                "fusion": fusion,
                "report": report,
                "bundle": bundle,
            }

        except Exception as e:

            print()
            print("=" * 70)
            print("❌ TRADING BRAIN FAILED")
            print("=" * 70)
            print(type(e).__name__)
            print(e)
            print("=" * 70)
            print()

            return {
                "success": False,
                "fusion": None,
                "report": None,
                "bundle": None,
                "error": str(e),
            }


if __name__ == "__main__":

    print()
    print("=" * 60)
    print("TRADING BRAIN READY")
    print("=" * 60)
