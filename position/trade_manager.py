"""
=========================================================
QUANT ULTRA
Trade Manager
=========================================================
Master controller for all open positions.
=========================================================
"""

from position.position_intelligence import PositionIntelligence
from position.trade_state_controller import TradeStateController
from position.trailing_stop_engine import TrailingStopEngine
from position.partial_exit_engine import PartialExitEngine


class TradeManager:

    def __init__(self):

        self.intelligence = PositionIntelligence()
        self.state = TradeStateController()
        self.trailing = TrailingStopEngine()
        self.partial = PartialExitEngine()

    # -------------------------------------------------

    def manage(self, position):

        report = {
            "actions": [],
            "position": position,
        }

        # ==========================================
        # Position Intelligence
        # ==========================================

        intelligence = self.intelligence.evaluate(position)

        position["health"] = intelligence["health"]
        position["recommended_action"] = intelligence["action"]
        position["broken_reasons"] = intelligence["reasons"]

        report["actions"].append(
            f"Health : {position['health']}"
        )

        # ==========================================
        # Trade State
        # ==========================================

        new_state = self.state.next_state(position)

        if new_state != position["state"]:

            report["actions"].append(
                f"State -> {new_state}"
            )

            position["state"] = new_state

        # ==========================================
        # Trailing Stop
        # ==========================================

        if str(position["state"]).endswith("TRAILING"):

            new_sl = self.trailing.calculate(position)

            if new_sl > position["stop_loss"]:

                report["actions"].append(
                    f"SL {position['stop_loss']} -> {new_sl}"
                )

                position["stop_loss"] = new_sl

        # ==========================================
        # Partial Exit
        # ==========================================

        partial = self.partial.evaluate(position)

        if partial["actions"]:
            report["actions"].extend(partial["actions"])

        # ==========================================
        # Exit Recommendation
        # ==========================================

        exit_trade = position["health"] < 40

        if exit_trade:
            report["actions"].append("EXIT TRADE")

        # ==========================================
        # Summary Fields
        # ==========================================

        report["health"] = position["health"]
        report["state"] = str(position["state"])
        report["confidence"] = position.get("confidence", 100)
        report["recommended_action"] = position["recommended_action"]
        report["stop_loss"] = position["stop_loss"]
        report["current_price"] = position["current_price"]
        report["pnl"] = position["pnl"]
        report["risk_multiple"] = position["risk_multiple"]
        report["exit"] = exit_trade

        print()
        print("=" * 60)
        print("🧠 TRADE MANAGER")
        print("=" * 60)
        print(f"Health      : {position['health']}")
        print(f"State       : {position['state']}")
        print(f"PnL         : ₹{position['pnl']}")
        print(f"Action      : {position['recommended_action']}")
        print(f"Stop Loss   : {position['stop_loss']}")
        print(f"Risk R      : {position['risk_multiple']}")
        print("=" * 60)

        return report


if __name__ == "__main__":

    print()
    print("=" * 60)
    print("TRADE MANAGER READY")
    print("=" * 60)
