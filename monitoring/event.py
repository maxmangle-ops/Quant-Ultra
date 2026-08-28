"""
=========================================================
QUANT ULTRA
Event Model
=========================================================
"""

from dataclasses import dataclass
from datetime import datetime

from monitoring.event_types import EventType


@dataclass
class Event:

    event_type: EventType

    source: str

    message: str

    data: dict

    timestamp: datetime = datetime.now()