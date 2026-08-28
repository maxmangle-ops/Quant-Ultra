"""
=========================================================
QUANT ULTRA
Market Intelligence Hub
=========================================================
"""

class MarketIntelligence:

    def __init__(self):

        pass

    # -------------------------------------------------

    def evaluate(

        self,

        guardian,

        vix,

        fii,

        gift,

        global_market,

        calendar,

    ):

        scores = []

        reasons = []

        # Guardian

        if guardian:

            scores.append(

                guardian.get(

                    "guardian_score",

                    50,

                )

            )

            reasons.extend(

                guardian.get(

                    "reasons",

                    [],

                )

            )

        # VIX

        if vix:

            scores.append(

                vix.get(

                    "score",

                    50,

                )

            )

            reasons.append(

                f"VIX : {vix['state']}"

            )

        # FII

        if fii:

            scores.append(

                fii.get(

                    "score",

                    50,

                )

            )

            reasons.extend(

                fii.get(

                    "reasons",

                    [],

                )

            )

        # Gift Nifty

        if gift:

            scores.append(

                gift.get(

                    "score",

                    50,

                )

            )

            reasons.extend(

                gift.get(

                    "reasons",

                    [],

                )

            )

        # Global

        if global_market:

            scores.append(

                global_market.get(

                    "score",

                    50,

                )

            )

            reasons.extend(

                global_market.get(

                    "reasons",

                    [],

                )

            )

        # Calendar

        if calendar:

            if not calendar["allowed"]:

                scores.append(0)

                reasons.append(

                    calendar["reason"]

                )

        # ---------------------------------------------

        if len(scores) == 0:

            final_score = 50

        else:

            final_score = round(

                sum(scores)

                / len(scores)

            )

        # ---------------------------------------------

        if final_score >= 80:

            bias = "STRONG BULLISH"

        elif final_score >= 65:

            bias = "BULLISH"

        elif final_score >= 40:

            bias = "NEUTRAL"

        elif final_score >= 20:

            bias = "BEARISH"

        else:

            bias = "STRONG BEARISH"

        return {

            "market_score": final_score,

            "market_bias": bias,

            "reasons": reasons,

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    hub = MarketIntelligence()

    report = hub.evaluate(

        guardian={

            "guardian_score":82,

            "reasons":["Healthy Trend"],

        },

        vix={

            "score":70,

            "state":"LOW",

        },

        fii={

            "score":75,

            "reasons":["FII Buying"],

        },

        gift={

            "score":65,

            "reasons":["Gap Up"],

        },

        global_market={

            "score":72,

            "reasons":["US Positive"],

        },

        calendar={

            "allowed":True,

            "reason":None,

        },

    )

    print()

    print("="*60)

    print("🧠 MARKET INTELLIGENCE")

    print("="*60)

    print(report)