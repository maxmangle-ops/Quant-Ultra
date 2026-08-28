"""
=========================================================
QUANT ULTRA
Position Intelligence
=========================================================
Enhanced Sprint 2 Version
=========================================================
"""

from position.health_engine import PositionHealthEngine


class PositionIntelligence:

    def __init__(self):
        self.health = PositionHealthEngine()

    # -------------------------------------------------

    def evaluate(self, position):

        result = self.health.evaluate(position)

        health = result["health"]

        confidence = self.calculate_confidence(position, health)

        action = self.action(health)

        report = {
            "health": health,
            "confidence": confidence,
            "reasons": result["reasons"],
            "action": action,
        }

        print()
        print("=" * 60)
        print("🧠 POSITION INTELLIGENCE")
        print("=" * 60)
        print(f"Health       : {health}")
        print(f"Confidence   : {confidence}")
        print(f"Action       : {action}")

        if report["reasons"]:
            print("Reasons")
            for reason in report["reasons"]:
                print(f" • {reason}")

        print("=" * 60)

        return report

    # -------------------------------------------------

    def calculate_confidence(self, position, health):

        confidence = health

        if position.get("risk_multiple", 0) >= 2:
            confidence += 5

        if position.get("pnl", 0) < 0:
            confidence -= 10

        confidence = max(0, min(100, confidence))

        position["confidence"] = confidence

        return confidence

    # -------------------------------------------------

    def action(self, health):

        if health >= 80:
            return "HOLD"

        if health >= 60:
            return "WATCH"

        if health >= 40:
            return "TRAIL"

        return "EXIT"


if __name__ == "__main__":

    print()
    print("=" * 60)
    print("POSITION INTELLIGENCE READY")
    print("=" * 60)
