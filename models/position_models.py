"""
=========================================================
QUANT ULTRA
Position Models
=========================================================
Canonical position object used throughout Quant Ultra.
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


# =========================================================
# Position
# =========================================================

@dataclass
class Position:

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    position_id: int

    symbol: str

    side: str

    # -----------------------------------------------------
    # Trade
    # -----------------------------------------------------

    entry: float

    quantity: int

    stop_loss: float

    target: float

    # -----------------------------------------------------
    # Status
    # -----------------------------------------------------

    status: str = "OPEN"

    state: str = "RUNNING"

    # -----------------------------------------------------
    # Live Prices
    # -----------------------------------------------------

    current_price: float = 0.0

    highest_price: float = 0.0

    lowest_price: float = 0.0

    # -----------------------------------------------------
    # Performance
    # -----------------------------------------------------

    pnl: float = 0.0

    pnl_percent: float = 0.0

    max_profit: float = 0.0

    max_drawdown: float = 0.0

    risk_multiple: float = 0.0

    # -----------------------------------------------------
    # Intelligence
    # -----------------------------------------------------

    health: int = 100

    confidence: int = 100

    # -----------------------------------------------------
    # Trade Thesis
    # -----------------------------------------------------

    entry_reasons: List[str] = field(default_factory=list)

    broken_reasons: List[str] = field(default_factory=list)

    # -----------------------------------------------------
    # Action Log
    # -----------------------------------------------------

    actions: List[str] = field(default_factory=list)

    # -----------------------------------------------------
    # Timing
    # -----------------------------------------------------

    opened_at: datetime = field(default_factory=datetime.now)

    last_updated: datetime = field(default_factory=datetime.now)

    closed_at: Optional[datetime] = None

    # -----------------------------------------------------
    # Exit
    # -----------------------------------------------------

    exit_price: Optional[float] = None

    exit_reason: Optional[str] = None

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    metadata: dict = field(default_factory=dict)

    # =====================================================
    # Convenience Properties
    # =====================================================

    @property
    def is_open(self):

        return self.status.upper() == "OPEN"

    @property
    def is_closed(self):

        return self.status.upper() == "CLOSED"

    @property
    def is_buy(self):

        return self.side.upper() == "BUY"

    @property
    def is_sell(self):

        return self.side.upper() == "SELL"

    # =====================================================
    # Helpers
    # =====================================================

    def add_action(self, action: str):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.actions.append(

            f"{timestamp} {action}"

        )

    def add_entry_reason(self, reason: str):

        self.entry_reasons.append(reason)

    def add_broken_reason(self, reason: str):

        self.broken_reasons.append(reason)

    def close(

        self,

        exit_price: float,

        reason: str,

    ):

        self.status = "CLOSED"

        self.state = "EXITED"

        self.exit_price = exit_price

        self.exit_reason = reason

        self.closed_at = datetime.now()

        self.add_action(

            f"Position Closed ({reason})"

        )

    def to_dict(self):

        """
        Compatibility layer for existing modules.
        """

        return self.__dict__.copy()


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    position = Position(

        position_id=1,

        symbol="NIFTY",

        side="BUY",

        entry=24250,

        quantity=25,

        stop_loss=24180,

        target=24450,

    )

    position.current_price = 24280

    position.pnl = 750

    position.add_entry_reason(

        "EMA Bullish"

    )

    position.add_action(

        "Trailing Stop Activated"

    )

    print()

    print("=" * 60)

    print("POSITION MODEL READY")

    print("=" * 60)

    print(position)