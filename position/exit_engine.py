"""
=========================================================
QUANT ULTRA
Exit Engine
=========================================================
Enhanced Sprint 2 Exit Engine
=========================================================
"""

from datetime import datetime


class ExitEngine:

    def evaluate(self, position):

        price = position["current_price"]
        stop = position["stop_loss"]
        target = position["target"]

        health = position.get("health", 100)
        confidence = position.get("confidence", 100)

        result = {
            "exit": False,
            "reason": None,
            "confidence": 100,
        }

        if price <= stop:
            result = {"exit": True, "reason": "STOP LOSS", "confidence": 100}

        elif price >= target:
            result = {"exit": True, "reason": "TARGET", "confidence": 100}

        elif health < 40:
            result = {"exit": True, "reason": "HEALTH", "confidence": 90}

        elif confidence < 35:
            result = {"exit": True, "reason": "CONFIDENCE", "confidence": 85}

        else:
            now = datetime.now()
            if now.hour == 15 and now.minute >= 20:
                result = {
                    "exit": True,
                    "reason": "MARKET CLOSE",
                    "confidence": 100,
                }

        print()
        print("=" * 60)
        print("🚪 EXIT ENGINE")
        print("=" * 60)
        print(f"Exit       : {result['exit']}")
        print(f"Reason     : {result['reason']}")
        print(f"Confidence : {result['confidence']}")
        print("=" * 60)

        return result


if __name__ == "__main__":
    print("=" * 60)
    print("EXIT ENGINE READY")
    print("=" * 60)
