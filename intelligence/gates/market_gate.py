"""
=========================================================
QUANT ULTRA
Market Gate
=========================================================
Evaluates overall market conditions before allowing a trade.
Supports both dictionary and model objects.
=========================================================
"""

from intelligence.gate_models import GateResult
from utils.model_helper import ModelHelper


class MarketGate:

    def __init__(self):

        self.pass_score = 70

    # -------------------------------------------------

    def evaluate(self, analysis):

        score = 0
        confidence = 0

        reasons = []
        warnings = []

        # -------------------------------------------------
        # Read Analysis (Dict / Object Compatible)
        # -------------------------------------------------

        market_score = ModelHelper.get(
            analysis,
            "market_score",
            0,
        )

        trend = str(
            ModelHelper.get(
                analysis,
                "trend",
                "NEUTRAL",
            )
        ).upper()

        analysis_confidence = ModelHelper.get(
            analysis,
            "confidence",
            0,
        )

        strategy = ModelHelper.get(
            analysis,
            "strategy",
            "UNKNOWN",
        )

        atr = ModelHelper.get(
            analysis,
            "atr",
            0,
        )

        # -------------------------------------------------
        # Market Score
        # -------------------------------------------------

        if market_score >= 80:

            score += 35
            confidence += 25

            reasons.append(
                "Strong Overall Market"
            )

        elif market_score >= 60:

            score += 20
            confidence += 15

            reasons.append(
                "Acceptable Market"
            )

        else:

            warnings.append(
                "Weak Market"
            )

        # -------------------------------------------------
        # Trend
        # -------------------------------------------------

        if trend != "NEUTRAL":

            score += 20
            confidence += 15

            reasons.append(
                "Clear Market Trend"
            )

        else:

            warnings.append(
                "Sideways Market"
            )

        # -------------------------------------------------
        # Confidence
        # -------------------------------------------------

        if analysis_confidence >= 80:

            score += 20
            confidence += 20

            reasons.append(
                "High Confidence Analysis"
            )

        elif analysis_confidence >= 60:

            score += 10
            confidence += 10

            reasons.append(
                "Moderate Confidence"
            )

        else:

            warnings.append(
                "Low Confidence"
            )

        # -------------------------------------------------
        # Strategy
        # -------------------------------------------------

        if strategy and str(strategy).upper() != "UNKNOWN":

            score += 10

            reasons.append(
                f"Strategy : {strategy}"
            )

        else:

            warnings.append(
                "No Strategy Selected"
            )

        # -------------------------------------------------
        # ATR
        # -------------------------------------------------

        if atr > 0:

            score += 10
            confidence += 10

            reasons.append(
                "Tradable Volatility"
            )

        else:

            warnings.append(
                "Low Volatility"
            )

        # -------------------------------------------------
        # Final
        # -------------------------------------------------

        score = min(score, 100)
        confidence = min(confidence, 100)

        result = GateResult(

            gate="Market",

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

    print("MARKET GATE READY")

    print("=" * 60)