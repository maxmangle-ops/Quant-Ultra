"""
=========================================================
QUANT ULTRA
Trade State
=========================================================
"""

from enum import Enum


class TradeState(Enum):

    SIGNAL = "SIGNAL"

    ANALYZING = "ANALYZING"

    WAITING_APPROVAL = "WAITING_APPROVAL"

    APPROVED = "APPROVED"

    ORDER_PENDING = "ORDER_PENDING"

    ACTIVE = "ACTIVE"

    PROTECTED = "PROTECTED"

    TRAILING = "TRAILING"

    PARTIAL_EXIT = "PARTIAL_EXIT"

    EXIT_PENDING = "EXIT_PENDING"

    CLOSED = "CLOSED"

    ARCHIVED = "ARCHIVED"


if __name__ == "__main__":

    print()

    print("=" * 60)

    print("TRADE STATE READY")

    print("=" * 60)

    for state in TradeState:

        print(state.value)