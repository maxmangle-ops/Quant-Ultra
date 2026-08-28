"""
=========================================================
QUANT ULTRA
Cost Engine
=========================================================
Calculates all trading costs and determines whether
the trade is worth taking after charges.
=========================================================
"""

from config.settings import (
    BROKERAGE_PER_ORDER,
    MIN_EXPECTED_NET_PROFIT,
)


class CostEngine:

    def __init__(self):

        self.brokerage = BROKERAGE_PER_ORDER

    # -----------------------------------------------------
    # Main Calculator
    # -----------------------------------------------------

    def calculate(
        self,
        buy_price,
        sell_price,
        quantity,
    ):

        turnover = (buy_price + sell_price) * quantity

        gross_profit = (sell_price - buy_price) * quantity

        # ---------------------------------------------
        # Brokerage
        # ---------------------------------------------

        brokerage = self.brokerage * 2

        # ---------------------------------------------
        # Exchange Charges
        # (Approximation)
        # ---------------------------------------------

        exchange_charge = turnover * 0.0000345

        # ---------------------------------------------
        # SEBI Charges
        # ---------------------------------------------

        sebi_charge = turnover * 0.000001

        # ---------------------------------------------
        # GST
        # ---------------------------------------------

        gst = (brokerage + exchange_charge) * 0.18

        # ---------------------------------------------
        # STT
        # (Approximation)
        # ---------------------------------------------

        stt = sell_price * quantity * 0.00025

        # ---------------------------------------------
        # Stamp Duty
        # (Approximation)
        # ---------------------------------------------

        stamp_duty = buy_price * quantity * 0.00003

        # ---------------------------------------------
        # Total Charges
        # ---------------------------------------------

        total_charges = (
            brokerage
            + exchange_charge
            + sebi_charge
            + gst
            + stt
            + stamp_duty
        )

        # ---------------------------------------------
        # Net Profit
        # ---------------------------------------------

        net_profit = gross_profit - total_charges

        # ---------------------------------------------
        # Cost %
        # ---------------------------------------------

        if gross_profit > 0:

            cost_percent = (
                total_charges / gross_profit
            ) * 100

        else:

            cost_percent = 100

        # ---------------------------------------------
        # Cost Score
        # ---------------------------------------------

        if cost_percent <= 10:

            score = 100

        elif cost_percent <= 20:

            score = 80

        elif cost_percent <= 30:

            score = 60

        elif cost_percent <= 50:

            score = 40

        else:

            score = 20

        # ---------------------------------------------
        # Decision
        # ---------------------------------------------

        approved = (
            net_profit >= MIN_EXPECTED_NET_PROFIT
        )

        if approved:

            reason = "Expected net profit is acceptable."

        else:

            reason = (
                "Expected profit too small after charges."
            )

        # ---------------------------------------------

        return {

            "Turnover": round(turnover, 2),

            "GrossProfit": round(gross_profit, 2),

            "Brokerage": round(brokerage, 2),

            "ExchangeCharges": round(exchange_charge, 2),

            "SEBI": round(sebi_charge, 2),

            "GST": round(gst, 2),

            "STT": round(stt, 2),

            "StampDuty": round(stamp_duty, 2),

            "Charges": round(total_charges, 2),

            "NetProfit": round(net_profit, 2),

            "CostPercent": round(cost_percent, 2),

            "CostScore": score,

            "Approved": approved,

            "Reason": reason,
        }


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    engine = CostEngine()

    report = engine.calculate(

        buy_price=100,

        sell_price=103,

        quantity=200,
    )

    print()

    print("=" * 55)
    print("💸 COST ENGINE")
    print("=" * 55)

    for key, value in report.items():

        print(f"{key:18}: {value}")