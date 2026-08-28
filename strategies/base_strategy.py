"""
=========================================================
QUANT ULTRA
Base Strategy
=========================================================
"""

from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def analyze(self, df):
        """
        Returns

        {
            "signal":"BUY",

            "confidence":85,

            "reasons":[]
        }
        """
        pass

    @abstractmethod
    def parameters(self):
        pass