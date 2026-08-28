"""
=========================================================
QUANT ULTRA
Account Models
=========================================================
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Account:
    """
    Represents the current trading account state.
    """

    broker: str

    available_cash: float

    available_margin: float

    used_margin: float

    buying_power: float

    pnl_today: float

    open_positions: int

    holdings: int

    open_orders: int

    last_updated: Optional[datetime] = None

    def __post_init__(self):

        if self.last_updated is None:
            self.last_updated = datetime.now()

    @property
    def total_margin(self):

        return self.available_margin + self.used_margin

    @property
    def utilization_percent(self):

        if self.total_margin == 0:
            return 0.0

        return round(
            (self.used_margin / self.total_margin) * 100,
            2,
        )

    def summary(self):

        return {
            "Broker": self.broker,
            "Available Cash": self.available_cash,
            "Available Margin": self.available_margin,
            "Used Margin": self.used_margin,
            "Buying Power": self.buying_power,
            "Today's P&L": self.pnl_today,
            "Open Positions": self.open_positions,
            "Holdings": self.holdings,
            "Open Orders": self.open_orders,
            "Margin Utilization": self.utilization_percent,
            "Last Updated": self.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
        }