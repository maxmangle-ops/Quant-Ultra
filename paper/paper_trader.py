"""
=========================================================
QUANT ULTRA
Paper Trading Engine
Version : 3.0
Status  : Runtime Owned
=========================================================
"""

from datetime import datetime

from journal.journal import save_trade
from position.position_manager import PositionManager
from models.trade_models import TradePlan


_runtime_paper_trader = None


class PaperTrader:

    def __init__(
        self,
        position_manager=None,
    ):

        if position_manager is None:

            position_manager = PositionManager()

        self.position_manager = position_manager

        self.open_trades = []
        self.closed_trades = []

    # -------------------------------------------------

    def open_trade(
        self,
        symbol=None,
        side=None,
        entry=None,
        stop_loss=None,
        target=None,
        quantity=None,
    ):

        trade_plan = (
            symbol
            if isinstance(symbol, TradePlan)
            else None
        )

        if trade_plan is not None:

            symbol = trade_plan.symbol
            side = trade_plan.side
            entry = trade_plan.entry
            stop_loss = trade_plan.stop_loss
            target = trade_plan.target
            quantity = trade_plan.quantity

        trade = {
            "TradeID": (
                len(self.open_trades)
                + len(self.closed_trades)
                + 1
            ),

            "Time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "Symbol": symbol,
            "Side": side,

            "Entry": round(
                entry,
                2,
            ),

            "StopLoss": round(
                stop_loss,
                2,
            ),

            "Target": round(
                target,
                2,
            ),

            "Quantity": quantity,

            "Status": "OPEN",

            "ExitPrice": None,

            "PnL": 0.0,
        }

        self.open_trades.append(
            trade,
        )

        save_trade(
            trade,
        )

        self.position_manager.open_position(

            symbol=symbol,

            side=side,

            entry=entry,

            quantity=quantity,

            stop_loss=stop_loss,

            target=target,
        )

        print()
        print("=" * 55)
        print("📄 PAPER TRADE OPENED")
        print("=" * 55)

        for key, value in trade.items():

            print(
                f"{key:15}: {value}"
            )

        print("=" * 55)

        return trade

    # -------------------------------------------------

    def close_trade(
        self,
        trade_id,
        exit_price,
    ):

        for trade in self.open_trades:

            if trade["TradeID"] != trade_id:
                continue

            trade["ExitPrice"] = round(
                exit_price,
                2,
            )

            trade["Status"] = "CLOSED"

            if trade["Side"] == "BUY":

                pnl = (
                    exit_price
                    - trade["Entry"]
                ) * trade["Quantity"]

            else:

                pnl = (
                    trade["Entry"]
                    - exit_price
                ) * trade["Quantity"]

            trade["PnL"] = round(
                pnl,
                2,
            )

            self.closed_trades.append(
                trade,
            )

            self.open_trades.remove(
                trade,
            )

            print()
            print("=" * 55)
            print("✅ PAPER TRADE CLOSED")
            print("=" * 55)
            print(
                f"Trade ID : {trade_id}"
            )
            print(
                f"Exit     : ₹{exit_price}"
            )
            print(
                f"PnL      : ₹{trade['PnL']}"
            )
            print("=" * 55)

            return trade

        print("Trade not found.")

        return None

    # -------------------------------------------------

    def get_open_trades(self):

        return self.open_trades

    # -------------------------------------------------

    def get_closed_trades(self):

        return self.closed_trades

    # -------------------------------------------------

    def has_open_position(self):

        return len(
            self.position_manager.get_open_positions()
        ) > 0

    # -------------------------------------------------

    def get_open_positions(self):

        return (
            self.position_manager
            .get_open_positions()
        )

    # -------------------------------------------------

    def get_position_manager(self):

        return self.position_manager


# =========================================================
# Runtime Compatibility Binding
# =========================================================

def configure_paper_trader(
    paper_trader,
):

    global _runtime_paper_trader

    if not isinstance(
        paper_trader,
        PaperTrader,
    ):

        raise TypeError(
            "configure_paper_trader() requires a PaperTrader instance."
        )

    _runtime_paper_trader = paper_trader


def _get_runtime_paper_trader():

    if _runtime_paper_trader is None:

        raise RuntimeError(
            "PaperTrader has not been registered with Runtime. "
            "Initialize Runtime before using the compatibility API."
        )

    return _runtime_paper_trader


def open_trade(
    symbol,
    side=None,
    entry=None,
    stop_loss=None,
    target=None,
    quantity=None,
):

    return _get_runtime_paper_trader().open_trade(

        symbol,

        side,

        entry,

        stop_loss,

        target,

        quantity,
    )


def has_open_position():

    return (
        _get_runtime_paper_trader()
        .has_open_position()
    )


def get_open_positions():

    return (
        _get_runtime_paper_trader()
        .get_open_positions()
    )


def get_position_manager():

    return (
        _get_runtime_paper_trader()
        .get_position_manager()
    )


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    trader = PaperTrader()

    trader.open_trade(

        symbol="NIFTY",

        side="BUY",

        entry=25000,

        stop_loss=24950,

        target=25100,

        quantity=1,
    )
