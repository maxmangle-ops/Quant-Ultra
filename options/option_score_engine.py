"""
=========================================================
QUANT ULTRA
Option Score Engine
=========================================================
Scores option contracts.
=========================================================
"""


class OptionScoreEngine:

    def __init__(self):
        pass

    # -------------------------------------------------

    def score(

        self,

        contract,

        atm,

        strike_step,

        technical_score,

    ):

        score = 0

        reasons = []

        # -----------------------------------------
        # Distance From ATM
        # -----------------------------------------

        distance = abs(

            contract.strike - atm

        )

        if distance == 0:

            score += 40

            reasons.append(
                "ATM Contract"
            )

        elif distance == strike_step:

            score += 30

            reasons.append(
                "Near ATM"
            )

        elif distance == strike_step * 2:

            score += 20

            reasons.append(
                "Within ATM Range"
            )

        # -----------------------------------------
        # Weekly Expiry
        # -----------------------------------------

        if contract.weekly:

            score += 10

            reasons.append(
                "Weekly Expiry"
            )

        # -----------------------------------------
        # Technical Confidence
        # -----------------------------------------

        tech = min(

            technical_score,

            100,

        )

        score += int(

            tech / 10

        )

        reasons.append(

            f"Technical {technical_score}"

        )

        return score, reasons


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("OPTION SCORE ENGINE READY")

    print("=" * 60)