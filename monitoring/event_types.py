"""
=========================================================
QUANT ULTRA
Event Types
=========================================================
"""

from enum import Enum


class EventType(Enum):

    SIGNAL_CREATED = "SIGNAL_CREATED"

    TRADE_APPROVED = "TRADE_APPROVED"

    ORDER_PLACED = "ORDER_PLACED"

    ORDER_FILLED = "ORDER_FILLED"

    POSITION_OPENED = "POSITION_OPENED"

    PRICE_UPDATED = "PRICE_UPDATED"

    POSITION_HEALTH = "POSITION_HEALTH"

    STATE_CHANGED = "STATE_CHANGED"

    STOP_MOVED = "STOP_MOVED"

    TARGET_CHANGED = "TARGET_CHANGED"

    PARTIAL_EXIT = "PARTIAL_EXIT"

    POSITION_CLOSED = "POSITION_CLOSED"

    JOURNAL_UPDATED = "JOURNAL_UPDATED"

    MARKET_OPEN = "MARKET_OPEN"

    MARKET_CLOSE = "MARKET_CLOSE"

    SYSTEM_ERROR = "SYSTEM_ERROR"


if __name__ == "__main__":

    print()

    print("=" * 60)

    print("EVENT TYPES READY")

    print("=" * 60)

    for event in EventType:

        print(event.value)