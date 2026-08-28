"""
=========================================================
QUANT ULTRA
Execution Gate
=========================================================
Final validation before sending order to broker.
Supports both dictionary and model objects.
=========================================================
"""

from intelligence.gate_models import GateResult
from utils.model_helper import ModelHelper


class ExecutionGate:

    def __init__(self):

        self.pass_score = 70

    # -------------------------------------------------

    def evaluate(

        self,

        trade_plan,

        execution_context,

    ):

        score = 0
        confidence = 0

        reasons = []
        warnings = []

        # -------------------------------------------------
        # Read Execution Context (Dict / Object Compatible)
        # -------------------------------------------------

        market_open = ModelHelper.get(
            execution_context,
            "market_open",
            False,
        )

        broker_connected = ModelHelper.get(
            execution_context,
            "broker_connected",
            False,
        )

        margin_available = ModelHelper.get(
            execution_context,
            "margin_available",
            False,
        )

        good_liquidity = ModelHelper.get(
            execution_context,
            "good_liquidity",
            False,
        )

        spread_ok = ModelHelper.get(
            execution_context,
            "spread_ok",
            False,
        )

        duplicate_position = ModelHelper.get(
            execution_context,
            "duplicate_position",
            False,
        )

        trading_allowed = ModelHelper.get(
            execution_context,
            "trading_allowed",
            False,
        )

        # -------------------------------------------------
        # Market Status
        # -------------------------------------------------

        if market_open:

            score += 20
            confidence += 15

            reasons.append(
                "Market Open"
            )

        else:

            warnings.append(
                "Market Closed"
            )

        # -------------------------------------------------
        # Broker Connection
        # -------------------------------------------------

        if broker_connected:

            score += 15
            confidence += 15

            reasons.append(
                "Broker Connected"
            )

        else:

            warnings.append(
                "Broker Offline"
            )

        # -------------------------------------------------
        # Margin
        # -------------------------------------------------

        if margin_available:

            score += 20
            confidence += 15

            reasons.append(
                "Margin Available"
            )

        else:

            warnings.append(
                "Insufficient Margin"
            )

        # -------------------------------------------------
        # Liquidity
        # -------------------------------------------------

        if good_liquidity:

            score += 15
            confidence += 10

            reasons.append(
                "Good Liquidity"
            )

        else:

            warnings.append(
                "Poor Liquidity"
            )

        # -------------------------------------------------
        # Spread
        # -------------------------------------------------

        if spread_ok:

            score += 10
            confidence += 10

            reasons.append(
                "Healthy Spread"
            )

        else:

            warnings.append(
                "Wide Spread"
            )

        # -------------------------------------------------
        # Duplicate Position
        # -------------------------------------------------

        if not duplicate_position:

            score += 10
            confidence += 10

            reasons.append(
                "No Duplicate Position"
            )

        else:

            warnings.append(
                "Position Already Exists"
            )

        # -------------------------------------------------
        # Trading Window
        # -------------------------------------------------

        if trading_allowed:

            score += 10
            confidence += 10

            reasons.append(
                "Trading Window Active"
            )

        else:

            warnings.append(
                "Outside Trading Hours"
            )

        # -------------------------------------------------
        # Final
        # -------------------------------------------------

        score = min(score, 100)
        confidence = min(confidence, 100)

        result = GateResult(

            gate="Execution",

            passed=score >= self.pass_score,

            score=score,

            confidence=confidence,

            blocking=True,

        )

        for reason in reasons:
            result.add_reason(reason)

        for warning in warnings:
            result.add_warning(warning)

        return result


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("EXECUTION GATE READY")

    print("=" * 60)