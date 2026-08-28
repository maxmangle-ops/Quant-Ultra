"""
=========================================================
QUANT ULTRA
Trade Models
Version : 2.1
=========================================================
Canonical TradePlan used by Decision, Risk and Execution.
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


# =========================================================
# Trade Plan
# =========================================================

@dataclass
class TradePlan:

    # -----------------------------------------------------
    # Instrument
    # -----------------------------------------------------

    symbol: str

    side: str

    # -----------------------------------------------------
    # Contract Metadata
    # -----------------------------------------------------

    instrument_key: str = ""

    trading_symbol: str = ""

    underlying: str = ""

    exchange: str = ""

    expiry: Optional[datetime] = None

    strike: float = 0.0

    option_type: str = ""

    lot_size: int = 0

    # -----------------------------------------------------
    # Trade Levels
    # -----------------------------------------------------

    entry: float = 0.0

    stop_loss: float = 0.0

    target: float = 0.0

    quantity: int = 0

    # -----------------------------------------------------
    # Capital
    # -----------------------------------------------------

    capital_used: float = 0.0

    risk_amount: float = 0.0

    expected_profit: float = 0.0

    expected_loss: float = 0.0

    reward_risk_ratio: float = 0.0

    # -----------------------------------------------------
    # Strategy
    # -----------------------------------------------------

    strategy: str = "UNKNOWN"

    confidence: int = 0

    technical_score: int = 0

    market_score: int = 0

    # -----------------------------------------------------
    # Cost Analysis
    # -----------------------------------------------------

    brokerage: float = 0.0

    taxes: float = 0.0

    charges: float = 0.0

    expected_net_profit: float = 0.0

    # -----------------------------------------------------
    # Decision
    # -----------------------------------------------------

    approved: bool = False

    rejection_reason: Optional[str] = None

    approval_reasons: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    # -----------------------------------------------------
    # Timing
    # -----------------------------------------------------

    created_at: datetime = field(default_factory=datetime.now)

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    metadata: dict = field(default_factory=dict)

    # =====================================================
    # Helper Methods
    # =====================================================

    def approve(self):

        self.approved = True

        self.rejection_reason = None

    # -----------------------------------------------------

    def reject(self, reason: str):

        self.approved = False

        self.rejection_reason = reason

    # -----------------------------------------------------

    def add_reason(self, reason: str):

        self.approval_reasons.append(reason)

    # -----------------------------------------------------

    def add_warning(self, warning: str):

        self.warnings.append(warning)

    # -----------------------------------------------------

    def apply_cost_report(self, cost_report: dict):
        """Copy values from the legacy CostEngine report."""

        self.brokerage = float(cost_report.get("Brokerage", 0.0))

        self.taxes = round(
            float(cost_report.get("GST", 0.0))
            + float(cost_report.get("SEBI", 0.0))
            + float(cost_report.get("STT", 0.0))
            + float(cost_report.get("StampDuty", 0.0)),
            2,
        )

        self.charges = float(cost_report.get("Charges", 0.0))

        self.expected_net_profit = float(
            cost_report.get("NetProfit", 0.0)
        )

    # -----------------------------------------------------

    @property
    def risk_percent(self):

        if self.capital_used <= 0:

            return 0.0

        return round(

            self.risk_amount /

            self.capital_used * 100,

            2,

        )

    # -----------------------------------------------------

    @property
    def is_option(self):

        return self.instrument_key.startswith("NSE_FO|")

    # -----------------------------------------------------

    @property
    def is_equity(self):

        return self.instrument_key.startswith("NSE_EQ|")

    # -----------------------------------------------------

    def to_dict(self):
        """
        Temporary compatibility layer for legacy modules.
        """

        return self.__dict__.copy()


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    trade = TradePlan(

        symbol="NIFTY",

        side="BUY",

        instrument_key="NSE_FO|123456",

        trading_symbol="NIFTY24JUL25000CE",

        underlying="NIFTY",

        exchange="NSE_FO",

        strike=25000,

        option_type="CE",

        lot_size=75,

        entry=120.50,

        stop_loss=105.00,

        target=150.00,

        quantity=75,

        capital_used=9037.50,

        risk_amount=1162.50,

        expected_profit=2212.50,

        expected_loss=1162.50,

        reward_risk_ratio=1.90,

        confidence=88,

        technical_score=82,

    )

    trade.add_reason("EMA Trend Confirmed")

    trade.add_reason("ATR Expansion")

    trade.approve()

    print()

    print("=" * 60)

    print("TRADE MODEL READY")

    print("=" * 60)

    print()

    print(trade)