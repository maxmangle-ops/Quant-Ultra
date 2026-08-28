"""
=========================================================
QUANT ULTRA
Gift Nifty Engine
=========================================================
"""

class GiftNiftyEngine:

    def __init__(self):

        pass

    # -------------------------------------------------

    def evaluate(

        self,

        previous_close,

        gift_nifty,

    ):

        gap = gift_nifty - previous_close

        gap_percent = (

            gap / previous_close

        ) * 100

        reasons = []

        score = 50

        # -------------------------------------------------

        if gap_percent >= 1:

            score += 30

            bias = "STRONG GAP UP"

            reasons.append("Large Gap Up Expected")

        elif gap_percent >= 0.30:

            score += 15

            bias = "GAP UP"

            reasons.append("Positive Opening")

        elif gap_percent <= -1:

            score -= 30

            bias = "STRONG GAP DOWN"

            reasons.append("Large Gap Down Expected")

        elif gap_percent <= -0.30:

            score -= 15

            bias = "GAP DOWN"

            reasons.append("Negative Opening")

        else:

            bias = "FLAT"

            reasons.append("Flat Opening Expected")

        return {

            "gift_nifty": gift_nifty,

            "previous_close": previous_close,

            "gap": round(gap, 2),

            "gap_percent": round(gap_percent, 2),

            "score": score,

            "bias": bias,

            "reasons": reasons,

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    engine = GiftNiftyEngine()

    result = engine.evaluate(

        previous_close=25150,

        gift_nifty=25320,

    )

    print()

    print("=" * 60)

    print("🌏 GIFT NIFTY")

    print("=" * 60)

    print(result)