"""
=========================================================
QUANT ULTRA
Partial Exit Engine
=========================================================
Enhanced Sprint 2 Version
=========================================================
"""


class PartialExitEngine:

    def evaluate(self, position):

        ltp = position["current_price"]
        entry = position["entry"]
        target = position["target"]
        quantity = position["quantity"]

        actions = []
        remaining = quantity

        milestones = position.setdefault(
            "milestones",
            {
                "breakeven": False,
                "partial1": False,
                "partial2": False,
                "runner": False,
            },
        )

        # -------------------------------------------------
        # 50% to Target
        # -------------------------------------------------

        level1 = entry + ((target - entry) * 0.50)

        if ltp >= level1 and not milestones["partial1"]:

            sell = max(1, int(quantity * 0.30))
            remaining -= sell
            milestones["partial1"] = True

            actions.append(
                {
                    "action": "SELL",
                    "quantity": sell,
                    "reason": "50% Target",
                }
            )

        # -------------------------------------------------
        # 75% to Target
        # -------------------------------------------------

        level2 = entry + ((target - entry) * 0.75)

        if ltp >= level2 and not milestones["partial2"]:

            sell = max(1, int(quantity * 0.20))
            remaining -= sell
            milestones["partial2"] = True

            actions.append(
                {
                    "action": "SELL",
                    "quantity": sell,
                    "reason": "75% Target",
                }
            )

        result = {
            "remaining": remaining,
            "actions": actions,
        }

        print()
        print("=" * 60)
        print("✂ PARTIAL EXIT ENGINE")
        print("=" * 60)

        if actions:
            for action in actions:
                print(
                    f"{action['action']} {action['quantity']} | {action['reason']}"
                )
        else:
            print("No Partial Exit")

        print(f"Remaining Qty : {remaining}")
        print("=" * 60)

        return result


if __name__ == "__main__":

    print()
    print("=" * 60)
    print("PARTIAL EXIT ENGINE READY")
    print("=" * 60)
