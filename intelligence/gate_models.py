"""
=========================================================
QUANT ULTRA
Gate Models
=========================================================
Canonical models used by all intelligence gates.
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict


# =========================================================
# Gate Result
# =========================================================

@dataclass
class GateResult:
    """
    Result returned by every gate.

    Example:
        Technical Gate
        Market Gate
        Risk Gate
        Cost Gate
        Execution Gate
    """

    gate: str

    passed: bool

    score: float

    confidence: float

    blocking: bool = False

    reasons: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    metadata: Dict = field(default_factory=dict)

    timestamp: datetime = field(default_factory=datetime.now)

    # -----------------------------------------------------

    def add_reason(self, reason: str):

        self.reasons.append(reason)

    # -----------------------------------------------------

    def add_warning(self, warning: str):

        self.warnings.append(warning)


# =========================================================
# Gate Bundle
# =========================================================

@dataclass
class GateBundle:
    """
    Collection of all gate results.
    """

    gates: List[GateResult] = field(default_factory=list)

    # -----------------------------------------------------

    def add(self, result: GateResult):

        self.gates.append(result)

    # -----------------------------------------------------

    @property
    def overall_score(self):

        if not self.gates:

            return 0.0

        return round(

            sum(g.score for g in self.gates)

            / len(self.gates),

            2,

        )

    # -----------------------------------------------------

    @property
    def overall_confidence(self):

        if not self.gates:

            return 0.0

        return round(

            sum(g.confidence for g in self.gates)

            / len(self.gates),

            2,

        )

    # -----------------------------------------------------

    @property
    def all_passed(self):

        return all(

            g.passed

            for g in self.gates

        )

    # -----------------------------------------------------

    @property
    def blocking_gate(self):

        for gate in self.gates:

            if gate.blocking and not gate.passed:

                return gate

        return None


# =========================================================
# Fusion Result
# =========================================================

@dataclass
class FusionResult:
    """
    Final output produced by Fusion Engine.
    """

    recommendation: str

    approved: bool

    score: float

    confidence: float

    gate_bundle: GateBundle

    reasons: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    timestamp: datetime = field(default_factory=datetime.now)

    # -----------------------------------------------------

    def add_reason(self, reason: str):

        self.reasons.append(reason)

    # -----------------------------------------------------

    def add_warning(self, warning: str):

        self.warnings.append(warning)


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    technical = GateResult(

        gate="Technical",

        passed=True,

        score=88,

        confidence=91,

    )

    technical.add_reason(

        "EMA Trend Confirmed"

    )

    risk = GateResult(

        gate="Risk",

        passed=True,

        score=96,

        confidence=98,

    )

    cost = GateResult(

        gate="Cost",

        passed=False,

        score=42,

        confidence=85,

        blocking=True,

    )

    cost.add_warning(

        "Expected profit too small"

    )

    bundle = GateBundle()

    bundle.add(technical)

    bundle.add(risk)

    bundle.add(cost)

    result = FusionResult(

        recommendation="WAIT",

        approved=False,

        score=bundle.overall_score,

        confidence=bundle.overall_confidence,

        gate_bundle=bundle,

    )

    print()

    print("=" * 60)

    print("GATE MODELS READY")

    print("=" * 60)

    print()

    print(result)