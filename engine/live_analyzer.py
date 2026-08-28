"""
=========================================================
QUANT ULTRA
Live Analyzer
=========================================================
"""

from config.settings import (
    EMA_FAST,
    EMA_SLOW,
    RSI_PERIOD,
    ATR_PERIOD,
    STRATEGY_NAME,
    SYMBOL_NAME,
    BUY_RSI,
    SELL_RSI,
)

from market.historical import get_historical_dataframe

from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.atr import calculate_atr
from indicators.vwap import calculate_vwap
from models.analysis_models import AnalysisResult


def analyze(symbol=None, timeframe="5minute"):

    # --------------------------------------------------
    # Default Symbol
    # --------------------------------------------------

    if symbol is None:
        symbol = SYMBOL_NAME

    # --------------------------------------------------
    # Load Historical Data
    # --------------------------------------------------

    df = get_historical_dataframe(
        symbol=symbol,
        timeframe=timeframe,
    )

    # --------------------------------------------------
    # No Data
    # --------------------------------------------------

    if df.empty:
        print(f"⚠️ No historical data for {symbol}")
        return None

    # --------------------------------------------------
    # Indicators
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Values
    # --------------------------------------------------

    price = float(latest["close"])

    ema_fast = float(latest[f"EMA{EMA_FAST}"])

    ema_slow = float(latest[f"EMA{EMA_SLOW}"])

    rsi = float(latest[f"RSI{RSI_PERIOD}"])

    atr = float(latest[f"ATR{ATR_PERIOD}"])

    vwap = float(latest["VWAP"])

    # --------------------------------------------------
    # Scores
    # --------------------------------------------------

    trend_score = 0
    momentum_score = 0
    volatility_score = 0
    vwap_score = 0

    reasons = []

    # Trend

    if ema_fast > ema_slow:

        trend = "BULLISH"

        trend_score = 30

        reasons.append("Bullish EMA Trend")

    else:

        trend = "BEARISH"

    # Momentum

    if rsi >= BUY_RSI:

        momentum_score = 20

        reasons.append("Strong RSI")

    elif rsi <= SELL_RSI:

        momentum_score = 20

        reasons.append("Weak RSI")

    # Volatility

    if atr > 1:

        volatility_score = 20

        reasons.append("Healthy ATR")

    # VWAP

    if price > vwap:

        vwap_score = 30

        reasons.append("Price Above VWAP")

    # --------------------------------------------------
    # Technical Score
    # --------------------------------------------------

    technical_score = (
        trend_score
        + momentum_score
        + volatility_score
        + vwap_score
    )

    # --------------------------------------------------
    # Market State
    # --------------------------------------------------

    if technical_score >= 80:

        market_state = "STRONG"

    elif technical_score >= 60:

        market_state = "GOOD"

    elif technical_score >= 40:

        market_state = "NEUTRAL"

    else:

        market_state = "WEAK"

    # --------------------------------------------------
    # Return
    # --------------------------------------------------

    signal = "WAIT"

    if (
        trend == "BULLISH"
        and rsi >= BUY_RSI
        and price > vwap
    ):
        signal = "BUY"

    elif (
        trend == "BEARISH"
        and rsi <= SELL_RSI
        and price < vwap
    ):
        signal = "SELL"

    return AnalysisResult(
        strategy=STRATEGY_NAME,
        symbol=symbol,
        price=round(price, 2),
        signal=signal,
        trend=trend,
        technical_score=technical_score,
        confidence=technical_score,
        atr=round(atr, 2),
        rsi=round(rsi, 2),
        ema_fast=round(ema_fast, 2),
        ema_slow=round(ema_slow, 2),
        reasons=reasons,
        metadata={
            "timeframe": timeframe,
            "vwap": round(vwap, 2),
            "trend_score": trend_score,
            "momentum_score": momentum_score,
            "volatility_score": volatility_score,
            "vwap_score": vwap_score,
            "market_state": market_state,
        },
    )


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    from pprint import pprint

    pprint(analyze())
