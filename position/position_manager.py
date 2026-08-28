"""
=========================================================
QUANT ULTRA
Position Manager
=========================================================
Maintains all live positions with trade lifecycle memory.
=========================================================
"""

from datetime import datetime

from position.trade_manager import TradeManager
from core.trade_state import TradeState


class PositionManager:

    def __init__(self):
        self.positions = []
        self.trade_manager = TradeManager()

    # -------------------------------------------------

    def open_position(self, symbol, side, entry, quantity, stop_loss, target):

        now = datetime.now()

        position = {
            "position_id": len(self.positions) + 1,
            "symbol": symbol,
            "side": side,

            "entry": entry,
            "quantity": quantity,
            "stop_loss": stop_loss,
            "target": target,

            "status": "OPEN",
            "state": TradeState.ACTIVE,

            "current_price": entry,
            "highest_price": entry,
            "lowest_price": entry,

            "pnl": 0.0,
            "pnl_percent": 0.0,
            "max_profit": 0.0,
            "max_drawdown": 0.0,
            "risk_multiple": 0.0,

            "health": 100,
            "confidence": 100,
            "recommended_action": "HOLD",
            "last_report": {},

            "entry_reasons": [],
            "broken_reasons": [],

            "milestones": {
                "breakeven": False,
                "partial1": False,
                "partial2": False,
                "runner": False,
            },

            "actions": [
                f"{now.strftime('%H:%M:%S')} Position Opened"
            ],

            "opened_at": now,
            "last_updated": now,
            "closed_at": None,

            "exit_reason": None,
            "exit_price": None,
        }

        self.positions.append(position)

        print()
        print("=" * 60)
        print("📍 POSITION OPENED")
        print("=" * 60)
        print(f"Position ID : {position['position_id']}")
        print(f"Symbol      : {position['symbol']}")
        print(f"Side        : {position['side']}")
        print(f"Entry       : {position['entry']}")
        print(f"Quantity    : {position['quantity']}")
        print(f"Stop Loss   : {position['stop_loss']}")
        print(f"Target      : {position['target']}")
        print("=" * 60)

        return position

    # -------------------------------------------------

    def update_price(self, symbol, ltp):

        now = datetime.now()

        for position in self.positions:

            if position["symbol"] != symbol or position["status"] != "OPEN":
                continue

            position["current_price"] = ltp
            position["last_updated"] = now

            position["highest_price"] = max(position["highest_price"], ltp)
            position["lowest_price"] = min(position["lowest_price"], ltp)

            if position["side"].upper() == "BUY":
                pnl = (ltp - position["entry"]) * position["quantity"]
            else:
                pnl = (position["entry"] - ltp) * position["quantity"]

            position["pnl"] = round(pnl, 2)

            investment = position["entry"] * position["quantity"]
            if investment > 0:
                position["pnl_percent"] = round((pnl / investment) * 100, 2)

            position["max_profit"] = max(position["max_profit"], round(pnl, 2))
            position["max_drawdown"] = min(position["max_drawdown"], round(pnl, 2))

            risk = abs(position["entry"] - position["stop_loss"]) * position["quantity"]
            if risk > 0:
                position["risk_multiple"] = round(pnl / risk, 2)

            report = self.trade_manager.manage(position)
            position["last_report"] = report

    # -------------------------------------------------

    def add_action(self, position_id, action):
        for position in self.positions:
            if position["position_id"] == position_id:
                position["actions"].append(
                    f"{datetime.now().strftime('%H:%M:%S')} {action}"
                )
                return

    # -------------------------------------------------

    def close_position(self, position_id, exit_reason="Manual"):
        for position in self.positions:
            if position["position_id"] == position_id:
                position["status"] = "CLOSED"
                position["state"] = TradeState.CLOSED
                position["closed_at"] = datetime.now()
                position["exit_price"] = position["current_price"]
                position["exit_reason"] = exit_reason
                self.add_action(position_id, f"Position Closed ({exit_reason})")
                return position
        return None

    # -------------------------------------------------

    def get_open_positions(self):
        return [p for p in self.positions if p["status"] == "OPEN"]

    def get_all_positions(self):
        return self.positions
