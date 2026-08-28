"""
=========================================================
QUANT ULTRA
News Guardian
=========================================================
"""

from datetime import datetime


class NewsGuardian:

    def __init__(self):

        self.news_score = 100

        self.events = []

    # -------------------------------------------------

    def evaluate(

        self,

        breaking_news=False,

        rbi_event=False,

        fed_event=False,

        earnings=False,

        war=False,

        election=False,

        fii_selloff=False,

        high_vix=False,

    ):

        score = 100

        reasons = []

        # -----------------------------------------

        if breaking_news:

            score -= 25

            reasons.append("Breaking Market News")

        if rbi_event:

            score -= 20

            reasons.append("RBI Policy Day")

        if fed_event:

            score -= 20

            reasons.append("US Fed Event")

        if earnings:

            score -= 15

            reasons.append("Major Earnings")

        if war:

            score -= 35

            reasons.append("Geopolitical Risk")

        if election:

            score -= 15

            reasons.append("Election Volatility")

        if fii_selloff:

            score -= 20

            reasons.append("Heavy FII Selling")

        if high_vix:

            score -= 20

            reasons.append("High India VIX")

        score = max(score, 0)

        if score >= 80:

            status = "SAFE"

        elif score >= 60:

            status = "CAUTION"

        elif score >= 40:

            status = "HIGH RISK"

        else:

            status = "NO TRADE"

        return {

            "guardian_score": score,

            "status": status,

            "reasons": reasons,

            "time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        }


# -------------------------------------------------

if __name__ == "__main__":

    guardian = NewsGuardian()

    report = guardian.evaluate(

        breaking_news=True,

        high_vix=True,

    )

    print()

    print("="*55)

    print("🛡 GUARDIAN AI")

    print("="*55)

    for k,v in report.items():

        print(f"{k:18}: {v}")