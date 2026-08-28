"""
=========================================================
QUANT ULTRA
Analysis Models
=========================================================
Canonical analysis objects used throughout Quant Ultra.
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


# =========================================================
# Analysis Result
# =========================================================

@dataclass
class AnalysisResult:
    """
    Represents the final output of a scanner/strategy.

    This object is passed from:

        Scanner
            ↓
        Intelligence
            ↓
        Decision
            ↓
        Execution
            ↓
        Dashboard
    """

    # -----------------------------------------------------
    # Instrument
    # -----------------------------------------------------

    symbol: str

    price: float

    timestamp: datetime = field(default_factory=datetime.now)

    # -----------------------------------------------------
    # Signal
    # -----------------------------------------------------

    signal: str = "WAIT"

    trend: str = "NEUTRAL"

    strategy: str = "UNKNOWN"

    # -----------------------------------------------------
    # Scores
    # -----------------------------------------------------

    technical_score: int = 0

    market_score: int = 0

    confidence: int = 0

    # -----------------------------------------------------
    # Indicators
    # -----------------------------------------------------

    atr: float = 0.0

    rsi: float = 0.0

    ema_fast: float = 0.0

    ema_slow: float = 0.0

    volume: float = 0.0

    # -----------------------------------------------------
    # Trade Levels
    # -----------------------------------------------------

    entry: float = 0.0

    stop_loss: float = 0.0

    target: float = 0.0

    support: float = 0.0

    resistance: float = 0.0

    # -----------------------------------------------------
    # Option Information
    # -----------------------------------------------------

    option_type: Optional[str] = None

    strike: Optional[float] = None

    expiry: Optional[str] = None

    # -----------------------------------------------------
    # Explanation
    # -----------------------------------------------------

    reasons: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    metadata: dict = field(default_factory=dict)

    # -----------------------------------------------------

    def add_reason(self, reason: str):

        self.reasons.append(reason)

    # -----------------------------------------------------

    def add_warning(self, warning: str):

        self.warnings.append(warning)

    # -----------------------------------------------------

    @property
    def bullish(self):

        return self.trend.upper() == "BULLISH"

    # -----------------------------------------------------

    @property
    def bearish(self):

        return self.trend.upper() == "BEARISH"

    # -----------------------------------------------------

    @property
    def approved(self):

        return self.signal.upper() in ("BUY", "SELL")

    # -----------------------------------------------------

    def to_dict(self):

        """
        Temporary compatibility layer.

        Existing modules that still expect dictionaries
        can continue working until migration is complete.
        """

        return self.__dict__.copy()


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    analysis = AnalysisResult(

        symbol="NIFTY",

        price=24500,

        signal="BUY",

        trend="BULLISH",

        technical_score=82,

        confidence=88,

    )

    analysis.add_reason("EMA Bullish Crossover")

    analysis.add_reason("ATR Expansion")

    print()

    print("=" * 60)

    print("ANALYSIS MODEL READY")

    print("=" * 60)

    print()

    print(analysis)

    print()

    print("Approved :", analysis.approved)

    print("Bullish  :", analysis.bullish)