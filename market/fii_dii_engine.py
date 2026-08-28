"""
=========================================================
QUANT ULTRA
FII DII Engine
=========================================================
"""

class FiiDiiEngine:

    def __init__(self):

        pass

    # -------------------------------------------------

    def evaluate(

        self,

        fii_net,

        dii_net,

    ):

        score = 50

        reasons = []

        # -----------------------------------------
        # FII
        # -----------------------------------------

        if fii_net > 0:

            score += 25

            reasons.append("FII Net Buyers")

        else:

            score -= 25

            reasons.append("FII Net Sellers")

        # -----------------------------------------
        # DII
        # -----------------------------------------

        if dii_net > 0:

            score += 10

            reasons.append("DII Net Buyers")

        else:

            score -= 10

            reasons.append("DII Net Sellers")

        # -----------------------------------------
        # Bias
        # -----------------------------------------

        if score >= 75:

            bias = "STRONG BULLISH"

        elif score >= 60:

            bias = "BULLISH"

        elif score >= 40:

            bias = "NEUTRAL"

        elif score >= 25:

            bias = "BEARISH"

        else:

            bias = "STRONG BEARISH"

        return {

            "score": score,

            "bias": bias,

            "fii_net": fii_net,

            "dii_net": dii_net,

            "reasons": reasons,

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    engine = FiiDiiEngine()

    result = engine.evaluate(

        fii_net=8200,

        dii_net=-1100,

    )

    print()

    print("=" * 60)

    print("🏦 FII / DII ENGINE")

    print("=" * 60)

    print(result)