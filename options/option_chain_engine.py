"""
=========================================================
QUANT ULTRA
Option Chain Engine
=========================================================
"""

class OptionChainEngine:

    def evaluate(

        self,

        pcr,

        call_oi,

        put_oi,

        max_pain,

        spot_price,

    ):

        score = 0

        reasons = []

        # ----------------------------------------
        # PCR
        # ----------------------------------------

        if 0.90 <= pcr <= 1.20:

            score += 25

            reasons.append("Healthy PCR")

        elif pcr > 1.40:

            score += 15

            reasons.append("Bullish PCR")

        elif pcr < 0.70:

            score += 15

            reasons.append("Bearish PCR")

        # ----------------------------------------
        # OI
        # ----------------------------------------

        if put_oi > call_oi:

            score += 35

            reasons.append("Put OI Stronger")

        else:

            score += 20

            reasons.append("Call OI Stronger")

        # ----------------------------------------
        # Max Pain
        # ----------------------------------------

        distance = abs(spot_price - max_pain)

        if distance < 100:

            score += 25

            reasons.append("Near Max Pain")

        elif distance < 200:

            score += 15

        # ----------------------------------------
        # Final
        # ----------------------------------------

        if score >= 70:

            status = "STRONG"

        elif score >= 50:

            status = "GOOD"

        else:

            status = "WEAK"

        return {

            "option_score": score,

            "status": status,

            "pcr": pcr,

            "max_pain": max_pain,

            "call_oi": call_oi,

            "put_oi": put_oi,

            "reasons": reasons,

        }


if __name__ == "__main__":

    engine = OptionChainEngine()

    result = engine.evaluate(

        pcr=1.08,

        call_oi=120000,

        put_oi=155000,

        max_pain=25100,

        spot_price=25140,

    )

    print()

    print("="*55)

    print("📊 OPTION CHAIN ENGINE")

    print("="*55)

    for k,v in result.items():

        print(f"{k:18}: {v}")