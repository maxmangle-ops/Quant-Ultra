"""
=========================================================
QUANT ULTRA
Decision Report
=========================================================
Produces a human-readable report from Fusion Result.
=========================================================
"""

from datetime import datetime


class DecisionReport:

    def __init__(self):

        pass

    # -------------------------------------------------

    def generate(

        self,

        fusion_result,

    ):

        report = {}

        report["timestamp"] = datetime.now()

        report["recommendation"] = fusion_result.recommendation

        report["approved"] = fusion_result.approved

        report["overall_score"] = fusion_result.score

        report["confidence"] = fusion_result.confidence

        report["gate_results"] = []

        # ---------------------------------------------
        # Gates
        # ---------------------------------------------

        for gate in fusion_result.gate_bundle.gates:

            report["gate_results"].append(

                {

                    "gate": gate.gate,

                    "passed": gate.passed,

                    "score": gate.score,

                    "confidence": gate.confidence,

                    "blocking": gate.blocking,

                    "reasons": gate.reasons,

                    "warnings": gate.warnings,

                }

            )

        report["reasons"] = fusion_result.reasons

        report["warnings"] = fusion_result.warnings

        return report

    # -------------------------------------------------

    def print_report(

        self,

        report,

    ):

        print()

        print("=" * 70)

        print("QUANT ULTRA DECISION REPORT")

        print("=" * 70)

        print()

        print(f"Recommendation : {report['recommendation']}")

        print(f"Approved      : {report['approved']}")

        print(f"Score         : {report['overall_score']}")

        print(f"Confidence    : {report['confidence']}%")

        print()

        print("-" * 70)

        print("GATE RESULTS")

        print("-" * 70)

        print()

        for gate in report["gate_results"]:

            status = "PASS" if gate["passed"] else "FAIL"

            print(

                f"{gate['gate']:<15}"

                f"{status:<8}"

                f"Score={gate['score']:<6}"

                f"Conf={gate['confidence']}"

            )

            for reason in gate["reasons"]:

                print(f"   ✓ {reason}")

            for warning in gate["warnings"]:

                print(f"   ⚠ {warning}")

            print()

        print("-" * 70)

        print("FUSION")

        print("-" * 70)

        print()

        for reason in report["reasons"]:

            print(f"✓ {reason}")

        for warning in report["warnings"]:

            print(f"⚠ {warning}")

        print()

        print("=" * 70)


# ---------------------------------------------------------

if __name__ == "__main__":

    from intelligence.gate_models import (
        GateBundle,
        GateResult,
        FusionResult,
    )

    bundle = GateBundle()

    bundle.add(

        GateResult(

            gate="Technical",

            passed=True,

            score=85,

            confidence=90,

            blocking=True,

            reasons=["EMA Bullish"],

        )

    )

    bundle.add(

        GateResult(

            gate="Risk",

            passed=True,

            score=95,

            confidence=98,

            blocking=True,

            reasons=["RR Excellent"],

        )

    )

    fusion = FusionResult(

        recommendation="BUY",

        approved=True,

        score=90,

        confidence=94,

        gate_bundle=bundle,

    )

    fusion.add_reason(

        "All blocking gates passed"

    )

    report_engine = DecisionReport()

    report = report_engine.generate(

        fusion

    )

    report_engine.print_report(

        report

    )