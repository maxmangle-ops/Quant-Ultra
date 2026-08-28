"""
=========================================================
QUANT ULTRA
Decision Engine
=========================================================
"""

from utils.model_helper import ModelHelper


class DecisionEngine:

    def __init__(self):

        pass

    # -----------------------------------------------------

    def calculate(

        self,

        analysis,

        trade,

        cost,

        margin,

        fusion=None,

    ):

        # ---------------------------------------------
        # Technical Score
        # ---------------------------------------------

        technical = ModelHelper.get(
            analysis,
            "technical_score",
            0,
        )

        signal = ModelHelper.get(
            analysis,
            "signal",
            "BUY",
        )

        # ---------------------------------------------

        risk = self.calculate_risk_score(
            trade,
        )

        # ---------------------------------------------
        # Cost Compatibility
        # ---------------------------------------------

        cost_score = ModelHelper.get(
            cost,
            "cost_score",
            ModelHelper.get(
                cost,
                "CostScore",
                0,
            ),
        )

        cost_approved = ModelHelper.get(
            cost,
            "approved",
            ModelHelper.get(
                cost,
                "Approved",
                True,
            ),
        )

        cost_reason = ModelHelper.get(
            cost,
            "reason",
            ModelHelper.get(
                cost,
                "Reason",
                "",
            ),
        )

        # ---------------------------------------------

        margin_score = self.calculate_margin_score(
            margin,
        )

        # ---------------------------------------------
        # Trade Quality
        # ---------------------------------------------

        trade_quality = round(

            technical * 0.40 +

            risk * 0.20 +

            cost_score * 0.20 +

            margin_score * 0.20

        )

        # ---------------------------------------------
        # Approval Rules
        # ---------------------------------------------

        approved = True

        reasons = []

        if signal == "WAIT":

            approved = False

            reasons.append(
                "No trading signal."
            )

        if not cost_approved:

            approved = False

            reasons.append(
                cost_reason
            )

        if not ModelHelper.get(
            margin,
            "approved",
            True,
        ):

            approved = False

            reasons.append(

                ModelHelper.get(
                    margin,
                    "reason",
                    "Margin rejected.",
                )

            )

        if trade_quality < 70:

            approved = False

            reasons.append(
                "Trade quality below threshold."
            )

        # ---------------------------------------------
        # Trading Brain Integration
        # ---------------------------------------------

        fusion_score = None
        fusion_confidence = None

        if fusion is not None:

            approved = approved and fusion.approved

            fusion_score = fusion.score

            fusion_confidence = fusion.confidence

            reasons.extend(
                fusion.reasons
            )

            for warning in fusion.warnings:

                reasons.append(
                    f"Fusion: {warning}"
                )

        # ---------------------------------------------

        recommendation = (

            "BUY"

            if approved

            else "WAIT"

        )

        # ---------------------------------------------

        return {

            "Technical": technical,

            "Risk": risk,

            "Cost": cost_score,

            "Margin": margin_score,

            "TradeQuality": trade_quality,

            "Recommendation": recommendation,

            "Approved": approved,

            "Reasons": reasons,

            # -----------------------------
            # Trading Brain
            # -----------------------------

            "FusionScore": fusion_score,

            "FusionConfidence": fusion_confidence,

        }

    # -----------------------------------------------------

    def from_fusion(self, analysis, trade, fusion, margin):
        """Expose the TradingBrain result without recomputing approval rules."""

        margin_approved = bool(ModelHelper.get(margin, "approved", False))
        approved = bool(fusion.approved and margin_approved)
        reasons = list(fusion.reasons)
        reasons.extend(f"Fusion: {warning}" for warning in fusion.warnings)

        if not margin_approved:
            reasons.append(ModelHelper.get(margin, "reason", "Margin rejected."))

        if approved:
            trade.approve()
        else:
            trade.reject("; ".join(reasons) or "Trading Brain rejected trade.")

        return {
            "Technical": ModelHelper.get(analysis, "technical_score", 0),
            "Risk": round(ModelHelper.get(trade, "risk_percent", 0), 2),
            "Cost": round(ModelHelper.get(trade, "expected_net_profit", 0), 2),
            "Margin": self.calculate_margin_score(margin),
            "TradeQuality": fusion.score,
            "Recommendation": fusion.recommendation if approved else "WAIT",
            "Approved": approved,
            "Reasons": reasons,
            "FusionScore": fusion.score,
            "FusionConfidence": fusion.confidence,
        }

    # -----------------------------------------------------

    def calculate_risk_score(

        self,

        trade,

    ):

        capital_used = ModelHelper.get(
            trade,
            "capital_used",
            0,
        )

        risk_amount = ModelHelper.get(
            trade,
            "risk_amount",
            0,
        )

        entry = ModelHelper.get(
            trade,
            "entry",
            0,
        )

        stop_loss = ModelHelper.get(
            trade,
            "stop_loss",
            0,
        )

        target = ModelHelper.get(
            trade,
            "target",
            0,
        )

        risk = entry - stop_loss
        reward = target - entry

        rr = reward / risk if risk > 0 else 0

        score = 100

        if capital_used > 50000:
            score -= 15

        if risk_amount > 1000:
            score -= 15

        if rr < 2:
            score -= 25

        return max(score, 20)

    # -----------------------------------------------------

    def calculate_margin_score(

        self,

        margin,

    ):

        utilization = ModelHelper.get(
            margin,
            "utilization",
            100,
        )

        if utilization < 40:
            return 100

        elif utilization < 60:
            return 80

        elif utilization < 80:
            return 60

        elif utilization < 90:
            return 40

        return 20


# ---------------------------------------------------------

if __name__ == "__main__":

    print("Decision Engine Ready")
