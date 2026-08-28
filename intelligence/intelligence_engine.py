"""
=========================================================
QUANT ULTRA
Intelligence Engine
=========================================================
"""

class IntelligenceEngine:

    def __init__(self):
        pass

    # -------------------------------------------------

    def evaluate(

        self,

        technical,

        market,

        portfolio,

        strategy,

        performance,

    ):

        score = 0

        reasons = []

        # -----------------------------------------
        # Technical
        # -----------------------------------------

        technical_score = technical.get(
            "technical_score",
            50,
        )

        score += technical_score * 0.35

        # -----------------------------------------
        # Market
        # -----------------------------------------

        market_score = market.get(
            "market_score",
            50,
        )

        score += market_score * 0.25

        # -----------------------------------------
        # Strategy
        # -----------------------------------------

        strategy_score = strategy.get(
            "confidence",
            50,
        )

        score += strategy_score * 0.20

        # -----------------------------------------
        # Performance
        # -----------------------------------------

        performance_score = performance.get(
            "score",
            50,
        )

        score += performance_score * 0.10

        # -----------------------------------------
        # Portfolio
        # -----------------------------------------

        portfolio_score = portfolio.get(
            "score",
            50,
        )

        score += portfolio_score * 0.10

        # -----------------------------------------

        score = round(score)

        # -----------------------------------------

        if score >= 85:

            confidence = "VERY HIGH"

        elif score >= 70:

            confidence = "HIGH"

        elif score >= 55:

            confidence = "MEDIUM"

        elif score >= 40:

            confidence = "LOW"

        else:

            confidence = "VERY LOW"

        reasons.append(

            f"Overall Intelligence Score : {score}"

        )

        return {

            "score": score,

            "confidence": confidence,

            "reasons": reasons,

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    engine = IntelligenceEngine()

    result = engine.evaluate(

        technical={

            "technical_score":82,

        },

        market={

            "market_score":75,

        },

        portfolio={

            "score":90,

        },

        strategy={

            "confidence":88,

        },

        performance={

            "score":70,

        },

    )

    print()

    print("=" * 60)

    print("🧠 INTELLIGENCE ENGINE")

    print("=" * 60)

    print(result)