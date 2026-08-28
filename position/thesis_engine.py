"""
=========================================================
QUANT ULTRA
Trade Thesis Engine
=========================================================
"""


class ThesisEngine:

    def build(

        self,

        analysis,

        market,

    ):

        thesis = []

        if analysis["trend"] == "BULLISH":
            thesis.append("Bullish Trend")

        if analysis["technical_score"] >= 70:
            thesis.append("Strong Technical")

        if market["score"] >= 70:
            thesis.append("Healthy Market")

        if analysis["atr"] > 0:
            thesis.append("Healthy ATR")

        return thesis