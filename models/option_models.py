"""
=========================================================
QUANT ULTRA
Option Models
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


# =========================================================
# OPTION CONTRACT
# =========================================================

@dataclass
class OptionContract:

    instrument_key: str

    trading_symbol: str

    strike: float

    option_type: str

    expiry: datetime

    weekly: bool

    lot_size: int

    exchange: str

    underlying: str


# =========================================================
# TRADE CANDIDATE
# =========================================================

@dataclass
class TradeCandidate:

    underlying: str

    spot_price: float

    trend: str

    technical_score: int

    contract: OptionContract

    confidence: int

    # -------------------------------------------------
    # Quant Ultra Scoring
    # -------------------------------------------------

    score: int = 0

    reasons: List[str] = field(default_factory=list)