"""
=========================================================
QUANT ULTRA
Risk Gate
=========================================================
Evaluates whether the proposed trade satisfies all
risk management rules.
Supports both dictionary and model objects.
=========================================================
"""

from intelligence.gate_models import GateResult
from utils.model_helper import ModelHelper


class RiskGate:

    def __init__(self):

        self.pass_score = 70

    # -------------------------------------------------

    def evaluate(self, trade_plan):

        score = 0
        confidence = 0

        reasons = []
        warnings = []

        # -------------------------------------------------
        # Read Trade (Dict / Object Compatible)
        # -------------------------------------------------

        rr = ModelHelper.get(
            trade_plan,
            "reward_risk_ratio",
            0,
        )

        risk_percent = ModelHelper.get(
            trade_plan,
            "risk_percent",
            100,
        )

        capital_used = ModelHelper.get(
            trade_plan,
            "capital_used",
            0,
        )

        expected_loss = ModelHelper.get(
            trade_plan,
            "expected_loss",
            0,
        )

        trade_confidence = ModelHelper.get(
            trade_plan,
            "confidence",
            0,
        )

        # -------------------------------------------------
        # Reward : Risk
        # -------------------------------------------------

        if rr >= 2.0:

            score += 30
            confidence += 25

            reasons.append(
                f"Excellent RR ({rr:.2f})"
            )

        elif rr >= 1.5:

            score += 20
            confidence += 18

            reasons.append(
                f"Good RR ({rr:.2f})"
            )

        else:

            warnings.append(
                f"Poor RR ({rr:.2f})"
            )

        # -------------------------------------------------
        # Risk %
        # -------------------------------------------------

        if risk_percent <= 2:

            score += 25
            confidence += 20

            reasons.append(
                "Risk Within Limit"
            )

        elif risk_percent <= 3:

            score += 15
            confidence += 12

            reasons.append(
                "Moderate Risk"
            )

        else:

            warnings.append(
                "Risk Too High"
            )

        # -------------------------------------------------
        # Capital Usage
        # -------------------------------------------------

        if capital_used > 0:

            score += 15
            confidence += 10

            reasons.append(
                "Capital Allocated"
            )

        else:

            warnings.append(
                "Invalid Capital Allocation"
            )

        # -------------------------------------------------
        # Expected Loss
        # -------------------------------------------------

        if expected_loss > 0:

            score += 10
            confidence += 8

            reasons.append(
                "Defined Maximum Loss"
            )

        else:

            warnings.append(
                "Undefined Maximum Loss"
            )

        # -------------------------------------------------
        # Trade Confidence
        # -------------------------------------------------

        if trade_confidence >= 80:

            score += 20
            confidence += 20

            reasons.append(
                "High Trade Confidence"
            )

        elif trade_confidence >= 60:

            score += 10
            confidence += 10

            reasons.append(
                "Moderate Trade Confidence"
            )

        else:

            warnings.append(
                "Low Trade Confidence"
            )

        # -------------------------------------------------
        # Final
        # -------------------------------------------------

        score = min(score, 100)
        confidence = min(confidence, 100)

        result = GateResult(

            gate="Risk",

            passed=score >= self.pass_score,

            score=score,

            confidence=confidence,

            blocking=True,

        )

        # -------------------------------------------------

        for reason in reasons:
            result.add_reason(reason)

        for warning in warnings:
            result.add_warning(warning)

        return result


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("RISK GATE READY")

    print("=" * 60)