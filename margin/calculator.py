"""
=========================================================
QUANT ULTRA
Margin & Capital Allocation Engine
=========================================================
"""

from dataclasses import dataclass


@dataclass
class MarginResult:

    approved: bool

    status: str

    utilization: float

    remaining_margin: float

    allocation_percent: float

    recommended_margin: float

    reason: str


class MarginEngine:

    def __init__(self):

        self.profiles = {

            "CONSERVATIVE": 40,

            "BALANCED": 65,

            "AGGRESSIVE": 85,
        }

    # -----------------------------------------------------

    def calculate(

        self,

        available_margin,

        required_margin,

        profile="BALANCED",

        guardian_score=80,

        technical_score=80,

    ):

        profile = profile.upper()

        if profile not in self.profiles:

            profile = "BALANCED"

        # ---------------------------------------------
        # Dynamic Allocation
        # ---------------------------------------------

        allocation = self.profiles[profile]

        # Guardian AI can reduce allocation

        if guardian_score < 60:

            allocation *= 0.50

        elif guardian_score < 75:

            allocation *= 0.75

        # Weak technical setup

        if technical_score < 70:

            allocation *= 0.80

        allocation = min(allocation, 90)

        usable_margin = (

            available_margin

            * allocation

            / 100

        )

        approved = usable_margin >= required_margin

        utilization = (

            required_margin

            / available_margin

        ) * 100

        remaining = max(

            available_margin - required_margin,

            0

        )

        if approved:

            status = "APPROVED"

            reason = "Enough buying power."

        else:

            status = "REJECTED"

            reason = "Insufficient usable margin."

        return MarginResult(

            approved=approved,

            status=status,

            utilization=round(utilization, 2),

            remaining_margin=round(remaining, 2),

            allocation_percent=round(allocation, 2),

            recommended_margin=round(usable_margin, 2),

            reason=reason,

        )


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    engine = MarginEngine()

    result = engine.calculate(

        available_margin=50000,

        required_margin=18000,

        profile="BALANCED",

        guardian_score=90,

        technical_score=88,

    )

    print()

    print("=" * 55)

    print("💼 MARGIN ENGINE")

    print("=" * 55)

    print(result)