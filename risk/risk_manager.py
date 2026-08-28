"""
=========================================================
QUANT ULTRA
Advanced Risk Manager
=========================================================
Calculates position sizing and returns the canonical
TradePlan used across Quant Ultra.
=========================================================
"""

from config.settings import (
    DEFAULT_RISK_PERCENT,
    RISK_REWARD_RATIO,
)

from models.trade_models import TradePlan


# =========================================================
# Risk Profiles
# =========================================================

RISK_PROFILES = {
    "CONSERVATIVE": 0.40,
    "BALANCED": 0.65,
    "AGGRESSIVE": 0.85,
}


# =========================================================
# Position Sizing
# =========================================================

def calculate_position(
    entry_price: float,
    atr: float,
    available_cash: float,
    buying_power: float,
    risk_percent: float = DEFAULT_RISK_PERCENT,
    profile: str = "BALANCED",
    symbol: str = "UNKNOWN",
    side: str = "BUY",
):

    profile = profile.upper()

    if profile not in RISK_PROFILES:
        profile = "BALANCED"

    # -----------------------------------------------------
    # Risk Amount
    # -----------------------------------------------------

    risk_amount = available_cash * (risk_percent / 100)

    # -----------------------------------------------------
    # Trade Levels
    # -----------------------------------------------------

    stop_loss = entry_price - atr

    target = entry_price + (atr * RISK_REWARD_RATIO)

    # -----------------------------------------------------
    # Position Size
    # -----------------------------------------------------

    risk_per_share = atr

    if risk_per_share <= 0:
        risk_per_share = 0.01

    risk_qty = int(risk_amount / risk_per_share)

    cash_qty = int(available_cash / entry_price)

    buying_power_qty = int(buying_power / entry_price)

    exposure_limit = buying_power * RISK_PROFILES[profile]

    exposure_qty = int(exposure_limit / entry_price)

    qty_map = {

        "Risk": risk_qty,

        "Cash": cash_qty,

        "Buying Power": buying_power_qty,

        "Exposure": exposure_qty,

    }

    limiting_factor = min(qty_map, key=qty_map.get)

    final_qty = max(1, qty_map[limiting_factor])

    # -----------------------------------------------------
    # Capital
    # -----------------------------------------------------

    capital_used = round(final_qty * entry_price, 2)

    expected_profit = round(
        (target - entry_price) * final_qty,
        2,
    )

    expected_loss = round(
        (entry_price - stop_loss) * final_qty,
        2,
    )

    reward_risk_ratio = round(

        expected_profit / expected_loss,

        2,

    ) if expected_loss > 0 else 0.0

    # -----------------------------------------------------
    # Canonical TradePlan
    # -----------------------------------------------------

    trade = TradePlan(

        # ---------------------------------------------
        # Instrument
        # ---------------------------------------------

        symbol=symbol,

        side=side.upper(),

        # ---------------------------------------------
        # Trade Levels
        # ---------------------------------------------

        entry=round(entry_price, 2),

        stop_loss=round(stop_loss, 2),

        target=round(target, 2),

        quantity=final_qty,

        # ---------------------------------------------
        # Capital
        # ---------------------------------------------

        capital_used=capital_used,

        risk_amount=round(risk_amount, 2),

        expected_profit=expected_profit,

        expected_loss=expected_loss,

        reward_risk_ratio=reward_risk_ratio,

        # ---------------------------------------------
        # Metadata
        # ---------------------------------------------

        metadata={

            "risk_qty": risk_qty,

            "cash_qty": cash_qty,

            "buying_power_qty": buying_power_qty,

            "exposure_qty": exposure_qty,

            "limiting_factor": limiting_factor,

            "profile": profile,

        },

    )

    return trade


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    trade = calculate_position(

        entry_price=1094.20,

        atr=1.74,

        available_cash=10000,

        buying_power=50000,

    )

    print()

    print("=" * 60)

    print("ADVANCED RISK MANAGER READY")

    print("=" * 60)

    print()

    print(trade)
