"""
=========================================================
QUANT ULTRA
Decision Models
=========================================================
"""

from dataclasses import dataclass
from typing import List


@dataclass
class EngineDecision:

    engine: str

    action: str

    confidence: int

    reason: str

    priority: int = 50


@dataclass
class FinalDecision:

    action: str

    confidence: int

    reasons: List[str]

    winning_engine: str