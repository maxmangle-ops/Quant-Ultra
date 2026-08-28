"""
=========================================================
QUANT ULTRA
Fusion Engine
=========================================================
Combines all intelligence gate results into one
final trading decision.
=========================================================
"""

from intelligence.gate_models import (
    GateBundle,
    FusionResult,
)


class FusionEngine:

    def __init__(self):

        self.minimum_score = 75

        self.minimum_confidence = 75

    # -------------------------------------------------

    def evaluate(

        self,

        gate_bundle: GateBundle,

    ) -> FusionResult:

        # =================================================
        # Stage 1
        # Hard Blocking
        # =================================================

        blocking_gate = gate_bundle.blocking_gate

        if blocking_gate is not None:

            result = FusionResult(

                recommendation="WAIT",

                approved=False,

                score=gate_bundle.overall_score,

                confidence=gate_bundle.overall_confidence,

                gate_bundle=gate_bundle,

            )

            result.add_reason(

                f"Blocked by {blocking_gate.gate} Gate"

            )

            result.add_warning(

                f"{blocking_gate.gate} Gate Failed"

            )

            return result

        # =================================================
        # Stage 2
        # Score Evaluation
        # =================================================

        score = gate_bundle.overall_score

        confidence = gate_bundle.overall_confidence

        approved = (

            score >= self.minimum_score

            and

            confidence >= self.minimum_confidence

        )

        recommendation = (

            "BUY"

            if approved

            else

            "WAIT"

        )

        result = FusionResult(

            recommendation=recommendation,

            approved=approved,

            score=score,

            confidence=confidence,

            gate_bundle=gate_bundle,

        )

        # -------------------------------------------------

        if approved:

            result.add_reason(

                "All Gates Passed"

            )

            result.add_reason(

                f"Score {score}"

            )

            result.add_reason(

                f"Confidence {confidence}%"

            )

        else:

            if score < self.minimum_score:

                result.add_warning(

                    "Overall score below threshold"

                )

            if confidence < self.minimum_confidence:

                result.add_warning(

                    "Confidence below threshold"

                )

        return result


# ---------------------------------------------------------

if __name__ == "__main__":

    from intelligence.gate_models import (

        GateBundle,

        GateResult,

    )

    bundle = GateBundle()

    bundle.add(

        GateResult(

            gate="Technical",

            passed=True,

            score=85,

            confidence=92,

            blocking=True,

        )

    )

    bundle.add(

        GateResult(

            gate="Market",

            passed=True,

            score=88,

            confidence=90,

            blocking=True,

        )

    )

    bundle.add(

        GateResult(

            gate="Risk",

            passed=True,

            score=93,

            confidence=95,

            blocking=True,

        )

    )

    bundle.add(

        GateResult(

            gate="Cost",

            passed=True,

            score=82,

            confidence=85,

            blocking=True,

        )

    )

    bundle.add(

        GateResult(

            gate="Execution",

            passed=True,

            score=95,

            confidence=97,

            blocking=True,

        )

    )

    engine = FusionEngine()

    result = engine.evaluate(

        bundle

    )

    print()

    print("=" * 60)

    print("FUSION ENGINE READY")

    print("=" * 60)

    print()

    print(result)