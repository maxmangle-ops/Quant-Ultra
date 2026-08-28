"""
=========================================================
QUANT ULTRA
Cost Gate
=========================================================
Validates whether a trade is worth taking after all
brokerage, taxes and charges.
Supports both dictionary and model objects.
=========================================================
"""

from intelligence.gate_models import GateResult
from utils.model_helper import ModelHelper


class CostGate:

    def __init__(self):

        self.minimum_score = 70
        self.minimum_net_profit = 100.0
        self.maximum_cost_percent = 20.0

    # -------------------------------------------------

    def evaluate(self, cost_report):

        score = 0
        confidence = 0

        reasons = []
        warnings = []

        # -------------------------------------------------
        # Read Cost Report (Dict / Object Compatible)
        # -------------------------------------------------

        approved = ModelHelper.get(
            cost_report,
            "approved",
            ModelHelper.get(
                cost_report,
                "Approved",
                False,
            ),
        )

        reason = ModelHelper.get(
            cost_report,
            "reason",
            ModelHelper.get(
                cost_report,
                "Reason",
                "",
            ),
        )

        net_profit = ModelHelper.get(
            cost_report,
            "net_profit",
            ModelHelper.get(
                cost_report,
                "NetProfit",
                0,
            ),
        )

        cost_percent = ModelHelper.get(
            cost_report,
            "cost_percent",
            ModelHelper.get(
                cost_report,
                "CostPercent",
                100,
            ),
        )

        cost_score = ModelHelper.get(
            cost_report,
            "cost_score",
            ModelHelper.get(
                cost_report,
                "CostScore",
                0,
            ),
        )

        # -------------------------------------------------
        # Cost Engine Approval
        # -------------------------------------------------

        if approved:

            score += 35
            confidence += 25

            reasons.append(
                "Cost Engine Approved"
            )

        else:

            warnings.append(
                reason or "Cost Engine Rejected Trade"
            )

        # -------------------------------------------------
        # Net Profit
        # -------------------------------------------------

        if net_profit >= self.minimum_net_profit:

            score += 30
            confidence += 25

            reasons.append(
                f"Net Profit ₹{net_profit:.2f}"
            )

        else:

            warnings.append(
                f"Low Net Profit ₹{net_profit:.2f}"
            )

        # -------------------------------------------------
        # Charges
        # -------------------------------------------------

        if cost_percent <= self.maximum_cost_percent:

            score += 20
            confidence += 20

            reasons.append(
                f"Charges {cost_percent:.2f}%"
            )

        else:

            warnings.append(
                f"High Charges {cost_percent:.2f}%"
            )

        # -------------------------------------------------
        # Cost Score
        # -------------------------------------------------

        score += min(cost_score, 15)

        confidence += min(
            cost_score / 2,
            15,
        )

        # -------------------------------------------------
        # Final
        # -------------------------------------------------

        score = min(score, 100)
        confidence = min(confidence, 100)

        result = GateResult(

            gate="Cost",

            passed=score >= self.minimum_score,

            score=score,

            confidence=confidence,

            blocking=True,

        )

        for r in reasons:
            result.add_reason(r)

        for w in warnings:
            result.add_warning(w)

        return result


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("COST GATE READY")

    print("=" * 60)