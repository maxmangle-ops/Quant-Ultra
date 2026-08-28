"""
=========================================================
QUANT ULTRA
Strategy Manager
=========================================================
"""

from strategies.ema_rsi_vwap import EmaRsiVwapStrategy


class StrategyManager:

    def __init__(self):

        self.strategies = {

            "EMA_RSI_VWAP": EmaRsiVwapStrategy(),

        }

    # -------------------------------------------------

    def names(self):

        return list(

            self.strategies.keys()

        )

    # -------------------------------------------------

    def get(self, name):

        return self.strategies[name]

    # -------------------------------------------------

    def analyze(

        self,

        strategy_name,

        dataframe,

    ):

        strategy = self.get(

            strategy_name,

        )

        return strategy.analyze(

            dataframe,

        )