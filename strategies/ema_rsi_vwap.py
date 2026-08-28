"""
=========================================================
QUANT ULTRA
EMA RSI VWAP Strategy
=========================================================
"""

from strategies.base_strategy import BaseStrategy

from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.atr import calculate_atr
from indicators.vwap import calculate_vwap

from config.settings import *


class EmaRsiVwapStrategy(BaseStrategy):

    def name(self):

        return "EMA_RSI_VWAP"

    def parameters(self):

        return {

            "ema_fast": EMA_FAST,

            "ema_slow": EMA_SLOW,

            "rsi": RSI_PERIOD,

            "atr": ATR_PERIOD,

        }

    def analyze(self, df):

        df[f"EMA{EMA_FAST}"] = calculate_ema(

            df["close"],

            EMA_FAST,

        )

        df[f"EMA{EMA_SLOW}"] = calculate_ema(

            df["close"],

            EMA_SLOW,

        )

        df[f"RSI{RSI_PERIOD}"] = calculate_rsi(

            df["close"],

            RSI_PERIOD,

        )

        df[f"ATR{ATR_PERIOD}"] = calculate_atr(

            df["high"],

            df["low"],

            df["close"],

            ATR_PERIOD,

        )

        df["VWAP"] = calculate_vwap(

            df["high"],

            df["low"],

            df["close"],

            df["volume"],

            df["time"],

        )

        latest = df.iloc[-1]

        reasons = []

        score = 0

        if latest[f"EMA{EMA_FAST}"] > latest[f"EMA{EMA_SLOW}"]:

            score += 30

            reasons.append("Bullish EMA")

        if latest[f"RSI{RSI_PERIOD}"] > BUY_RSI:

            score += 20

            reasons.append("Bullish RSI")

        if latest["close"] > latest["VWAP"]:

            score += 30

            reasons.append("Above VWAP")

        if latest[f"ATR{ATR_PERIOD}"] > 1:

            score += 20

            reasons.append("Healthy ATR")

        if score >= 80:

            signal = "BUY"

        elif score <= 20:

            signal = "SELL"

        else:

            signal = "WAIT"

        return {

            "strategy": self.name(),

            "signal": signal,

            "confidence": score,

            "reasons": reasons,

        }