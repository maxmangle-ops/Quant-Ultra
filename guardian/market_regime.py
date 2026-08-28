"""
=========================================================
QUANT ULTRA
Market Regime Engine
=========================================================
"""

from enum import Enum


class MarketRegime(Enum):

    TRENDING_UP = "TRENDING_UP"

    TRENDING_DOWN = "TRENDING_DOWN"

    RANGE = "RANGE"

    HIGH_VOLATILITY = "HIGH_VOLATILITY"

    LOW_VOLATILITY = "LOW_VOLATILITY"

    EVENT_DAY = "EVENT_DAY"


class MarketRegimeEngine:

    def detect(

        self,

        technical_score,

        atr,

        ema_fast,

        ema_slow,

    ):

        if atr > 3:

            return MarketRegime.HIGH_VOLATILITY

        if atr < 0.8:

            return MarketRegime.LOW_VOLATILITY

        if ema_fast > ema_slow:

            if technical_score >= 80:

                return MarketRegime.TRENDING_UP

        if ema_fast < ema_slow:

            if technical_score <= 30:

                return MarketRegime.TRENDING_DOWN

        return MarketRegime.RANGE


if __name__ == "__main__":

    engine = MarketRegimeEngine()

    regime = engine.detect(

        technical_score=85,

        atr=1.9,

        ema_fast=250,

        ema_slow=220,

    )

    print()

    print("="*50)

    print("MARKET REGIME")

    print("="*50)

    print(regime.value)