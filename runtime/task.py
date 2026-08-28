"""
=========================================================
QUANT ULTRA
Scheduled Task
=========================================================
Represents a schedulable task inside Quant Ultra.
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Callable, Any


@dataclass
class Task:

    # -------------------------------------------------
    # Basic
    # -------------------------------------------------

    name: str

    callback: Callable[..., Any]

    interval: float

    enabled: bool = True

    # -------------------------------------------------
    # Runtime
    # -------------------------------------------------

    last_run: datetime | None = None

    next_run: datetime | None = None

    total_runs: int = 0

    total_failures: int = 0

    average_runtime: float = 0.0

    last_runtime: float = 0.0

    priority: int = 100

    metadata: dict = field(default_factory=dict)

    # -------------------------------------------------

    def enable(self):

        self.enabled = True

    # -------------------------------------------------

    def disable(self):

        self.enabled = False

    # -------------------------------------------------

    def __str__(self):

        return (

            f"Task(name={self.name}, "

            f"interval={self.interval}s, "

            f"enabled={self.enabled})"

        )


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("TASK MODEL READY")

    print("=" * 60)

    task = Task(

        name="Scanner",

        callback=lambda: None,

        interval=60,

    )

    print(task)