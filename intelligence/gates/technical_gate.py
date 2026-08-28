"""
=========================================================
QUANT ULTRA
Technical Gate
=========================================================
Evaluates all technical indicators and returns a GateResult.
Supports both dictionary and model objects.
=========================================================
"""

from intelligence.gate_models import GateResult
from utils.model_helper import ModelHelper


class TechnicalGate:

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

        trend = str(
            ModelHelper.get(
                analysis,
                "trend",
                "NEUTRAL",
            )
        ).upper()

        technical_score = ModelHelper.get(
            analysis,
            "technical_score",
            0,
        )

        rsi = ModelHelper.get(
            analysis,
            "rsi",
            0,
        )

        atr = ModelHelper.get(
            analysis,
            "atr",
            0,
        )

        ema_fast = ModelHelper.get(
            analysis,
            "ema_fast",
            0,
        )

        ema_slow = ModelHelper.get(
            analysis,
            "ema_slow",
            0,
        )

        volume = ModelHelper.get(
            analysis,
            "volume",
            0,
        )

        # -------------------------------------------------
        # Trend
        # -------------------------------------------------

        if trend == "BULLISH":

            score += 20
            confidence += 15

            reasons.append(
                "Bullish Trend"
            )

        elif trend == "BEARISH":

            score += 20
            confidence += 15

            reasons.append(
                "Bearish Trend"
            )

        else:

            warnings.append(
                "No Clear Trend"
            )

        # -------------------------------------------------
        # Technical Score
        # -------------------------------------------------

        score += min(
            technical_score,
            40,
        )

        confidence += min(
            technical_score / 2,
            20,
        )

        # -------------------------------------------------
        # RSI
        # -------------------------------------------------

        if rsi > 0:

            if 45 <= rsi <= 65:

                score += 10
                confidence += 8

                reasons.append(
                    "Healthy RSI"
                )

            elif rsi > 75:

                warnings.append(
                    "Overbought RSI"
                )

            elif rsi < 25:

                warnings.append(
                    "Oversold RSI"
                )

        # -------------------------------------------------
        # ATR
        # -------------------------------------------------

        if atr > 0:

            score += 8
            confidence += 5

            reasons.append(
                "Healthy ATR"
            )

        # -------------------------------------------------
        # EMA
        # -------------------------------------------------

        if ema_fast > 0 and ema_slow > 0:

            if ema_fast > ema_slow:

                score += 12
                confidence += 10

                reasons.append(
                    "Bullish EMA Alignment"
                )

            elif ema_fast < ema_slow:

                warnings.append(
                    "Bearish EMA Alignment"
                )

        # -------------------------------------------------
        # Volume
        # -------------------------------------------------

        if volume > 0:

            score += 10
            confidence += 7

            reasons.append(
                "Volume Confirmation"
            )

        # -------------------------------------------------
        # Final Score
        # -------------------------------------------------

        score = min(score, 100)
        confidence = min(confidence, 100)

        result = GateResult(

            gate="Technical",

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

    print("TECHNICAL GATE READY")

    print("=" * 60)