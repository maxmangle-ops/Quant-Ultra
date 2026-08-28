"""
=========================================================
QUANT ULTRA
Execution Context
=========================================================
Runtime execution information supplied to the
Execution Gate.
=========================================================
"""

from dataclasses import dataclass


@dataclass
class ExecutionContext:

    # -----------------------------------------
    # Market
    # -----------------------------------------

    market_open: bool = True

    trading_allowed: bool = True

    # -----------------------------------------
    # Broker
    # -----------------------------------------

    broker_connected: bool = True

    margin_available: bool = True

    # -----------------------------------------
    # Execution
    # -----------------------------------------

    good_liquidity: bool = True

    spread_ok: bool = True

    duplicate_position: bool = False

    # -----------------------------------------
    # Optional Runtime Information
    # -----------------------------------------

    exchange: str = "NSE"

    broker: str = "UPSTOX"

    remarks: str = ""