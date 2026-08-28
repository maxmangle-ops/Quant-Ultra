"""
=========================================================
QUANT ULTRA
Position Health Engine
=========================================================
"""

class PositionHealthEngine:

    def evaluate(

        self,

        position,

    ):

        score = 100

        reasons = []

        # ---------------------------------
        # Losing Money
        # ---------------------------------

        if position["pnl"] < 0:

            score -= 10

            reasons.append(
                "Negative PnL"
            )

        # ---------------------------------
        # Drawdown
        # ---------------------------------

        if position["max_drawdown"] < -500:

            score -= 20

            reasons.append(
                "High Drawdown"
            )

        # ---------------------------------
        # Risk Multiple
        # ---------------------------------

        if position["risk_multiple"] < -1:

            score -= 20

            reasons.append(
                "Risk Exceeded"
            )

        # ---------------------------------
        # Healthy Trade
        # ---------------------------------

        if position["max_profit"] > 0:

            score += 5

        score = max(

            0,

            min(score,100)

        )

        return {

            "health":score,

            "reasons":reasons,

        }


if __name__=="__main__":

    print()

    print("="*60)

    print("POSITION HEALTH ENGINE READY")

    print("="*60)