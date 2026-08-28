class TradeQualityEngine:

    def __init__(
        self,
        technical_score,
        risk_score,
        cost_score,
        margin_score,
    ):
        self.technical_score = technical_score
        self.risk_score = risk_score
        self.cost_score = cost_score
        self.margin_score = margin_score

    def calculate(self):

        weights = {
            "technical": 0.40,
            "risk": 0.25,
            "cost": 0.15,
            "margin": 0.20,
        }

        final_score = (
            self.technical_score * weights["technical"]
            + self.risk_score * weights["risk"]
            + self.cost_score * weights["cost"]
            + self.margin_score * weights["margin"]
        )

        if final_score >= 90:
            recommendation = "🟢 ELITE TRADE"

        elif final_score >= 80:
            recommendation = "🟢 STRONG BUY"

        elif final_score >= 70:
            recommendation = "🔵 BUY"

        elif final_score >= 60:
            recommendation = "🟡 WATCH"

        else:
            recommendation = "🔴 REJECT"

        return {
            "TradeQuality": round(final_score, 2),
            "Recommendation": recommendation,
        }


if __name__ == "__main__":

    engine = TradeQualityEngine(
        technical_score=88,
        risk_score=95,
        cost_score=90,
        margin_score=85,
    )

    print(engine.calculate())