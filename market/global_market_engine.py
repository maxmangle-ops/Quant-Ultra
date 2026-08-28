"""
=========================================================
QUANT ULTRA
Global Market Engine
=========================================================
"""

class GlobalMarketEngine:

    def __init__(self):

        pass

    # -------------------------------------------------

    def evaluate(

        self,

        dow_change,

        nasdaq_change,

        sp500_change,

        nikkei_change,

        hangseng_change,

    ):

        score = 50

        reasons = []

        markets = [

            ("Dow", dow_change),

            ("Nasdaq", nasdaq_change),

            ("S&P500", sp500_change),

            ("Nikkei", nikkei_change),

            ("Hang Seng", hangseng_change),

        ]

        for name, change in markets:

            if change > 1:

                score += 10

                reasons.append(f"{name} Strong Bullish")

            elif change > 0:

                score += 5

                reasons.append(f"{name} Bullish")

            elif change < -1:

                score -= 10

                reasons.append(f"{name} Strong Bearish")

            elif change < 0:

                score -= 5

                reasons.append(f"{name} Bearish")

        score = max(0, min(score, 100))

        # -----------------------------------------

        if score >= 75:

            sentiment = "STRONG BULLISH"

        elif score >= 60:

            sentiment = "BULLISH"

        elif score >= 40:

            sentiment = "NEUTRAL"

        elif score >= 25:

            sentiment = "BEARISH"

        else:

            sentiment = "STRONG BEARISH"

        return {

            "score": score,

            "sentiment": sentiment,

            "reasons": reasons,

            "markets": {

                "Dow": dow_change,

                "Nasdaq": nasdaq_change,

                "S&P500": sp500_change,

                "Nikkei": nikkei_change,

                "Hang Seng": hangseng_change,

            }

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    engine = GlobalMarketEngine()

    result = engine.evaluate(

        dow_change=0.85,

        nasdaq_change=1.42,

        sp500_change=0.67,

        nikkei_change=-0.22,

        hangseng_change=0.91,

    )

    print()

    print("=" * 60)

    print("🌍 GLOBAL MARKET ENGINE")

    print("=" * 60)

    print(result)