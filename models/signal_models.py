"""
=========================================================
QUANT ULTRA
Signal Models
=========================================================
Canonical intelligence models used throughout Quant Ultra.
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict


# =========================================================
# Signal Vote
# =========================================================

@dataclass
class SignalVote:
    """
    Opinion produced by one analysis engine.

    Example:
        EMA
        RSI
        ATR
        VWAP
        Risk
        Cost
    """

    source: str

    category: str

    direction: str

    score: float

    confidence: float

    weight: float = 1.0

    reason: str = ""

    timestamp: datetime = field(default_factory=datetime.now)

    metadata: Dict = field(default_factory=dict)


# =========================================================
# Signal Bundle
# =========================================================

@dataclass
class SignalBundle:
    """
    Collection of votes from all engines.
    """

    votes: List[SignalVote] = field(default_factory=list)

    def add_vote(self, vote: SignalVote):

        self.votes.append(vote)

    @property
    def total_score(self):

        return sum(

            vote.score * vote.weight

            for vote in self.votes

        )

    @property
    def average_confidence(self):

        if not self.votes:

            return 0.0

        return round(

            sum(

                vote.confidence

                for vote in self.votes

            )

            / len(self.votes),

            2,

        )


# =========================================================
# Decision
# =========================================================

@dataclass
class Decision:

    recommendation: str

    score: float

    confidence: float

    approved: bool

    reasons: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    timestamp: datetime = field(default_factory=datetime.now)


# =========================================================
# Decision Report
# =========================================================

@dataclass
class DecisionReport:

    bundle: SignalBundle

    decision: Decision

    execution_time_ms: float = 0.0

    metadata: Dict = field(default_factory=dict)


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    ema = SignalVote(

        source="EMA",

        category="TREND",

        direction="BUY",

        score=20,

        confidence=92,

        reason="EMA20 crossed EMA50",

    )

    rsi = SignalVote(

        source="RSI",

        category="MOMENTUM",

        direction="BUY",

        score=8,

        confidence=84,

        reason="Recovered from oversold",

    )

    bundle = SignalBundle()

    bundle.add_vote(ema)

    bundle.add_vote(rsi)

    decision = Decision(

        recommendation="BUY",

        score=bundle.total_score,

        confidence=bundle.average_confidence,

        approved=True,

        reasons=[

            "Overall score above threshold"

        ],

    )

    report = DecisionReport(

        bundle=bundle,

        decision=decision,

    )

    print()

    print("=" * 60)

    print("SIGNAL MODELS READY")

    print("=" * 60)

    print()

    print(report)