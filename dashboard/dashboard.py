"""
=========================================================
QUANT ULTRA
Dashboard
=========================================================
"""

from datetime import datetime
from utils.model_helper import ModelHelper


class Dashboard:

    def __init__(self):
        pass

    def display(
        self,
        account,
        analysis,
        intelligence,
        decision,
        portfolio,
    ):

        print()
        print("=" * 80)
        print("🚀 QUANT ULTRA LIVE DASHBOARD")
        print("=" * 80)
        print()
        print("⏰", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        print()
        print("-" * 80)
        print("ACCOUNT")
        print("-" * 80)
        print(f"Broker            : {account.get('broker','-')}")
        print(f"Cash              : ₹{account.get('cash',0):,.2f}")
        print(f"Margin            : ₹{account.get('margin',0):,.2f}")
        print(f"Buying Power      : ₹{account.get('buying_power',0):,.2f}")

        print()
        print("-" * 80)
        print("MARKET")
        print("-" * 80)

        print(f"Symbol            : {ModelHelper.get(analysis,'symbol')}")
        print(f"Price             : ₹{ModelHelper.get(analysis,'price')}")
        print(f"Trend             : {ModelHelper.get(analysis,'trend')}")
        print(f"Technical Score   : {ModelHelper.get(analysis,'technical_score')}")
        print(f"Market Score      : {intelligence['market_score']}")
        print(f"Market Bias       : {intelligence['market_bias']}")

        print()
        print("-" * 80)
        print("PORTFOLIO")
        print("-" * 80)
        print(f"Open Positions    : {portfolio.get('positions',0)}")
        print(f"Capital Used      : ₹{portfolio.get('capital_used',0):,.2f}")
        print(f"Risk Used         : ₹{portfolio.get('risk',0):,.2f}")

        print()
        print("-" * 80)
        print("DECISION")
        print("-" * 80)
        print(f"Recommendation    : {decision['Recommendation']}")
        print(f"Trade Quality     : {decision['TradeQuality']}")
        print(f"Approved          : {decision['Approved']}")

        print()
        print("-" * 80)
        print("SCORE BREAKDOWN")
        print("-" * 80)
        print(f"Technical         : {decision.get('Technical','-')}")
        print(f"Risk              : {decision.get('Risk','-')}")
        print(f"Cost              : {decision.get('Cost','-')}")
        print(f"Margin            : {decision.get('Margin','-')}")

        print()
        print("-" * 80)
        print("MARKET REASONS")
        print("-" * 80)

        if intelligence.get("reasons"):
            for reason in intelligence["reasons"]:
                print("🌍", reason)
        else:
            print("No market reasons available.")

        print()
        print("-" * 80)
        print("TECHNICAL REASONS")
        print("-" * 80)

        for reason in ModelHelper.get(analysis, "reasons", []):
            print("📈", reason)

        print()
        print("-" * 80)
        print("DECISION REASONS")
        print("-" * 80)

        if decision.get("Reasons"):
            for reason in decision["Reasons"]:
                print("❌", reason)
        else:
            print("✅ Trade Passed All Checks")

        print()
        print("=" * 80)
