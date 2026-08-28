"""
=========================================================
QUANT ULTRA
Global Configuration
=========================================================
DO NOT hardcode values anywhere else.

Every engine should import settings from here.
=========================================================
"""

# =========================================================
# PROJECT
# =========================================================

PROJECT_NAME = "Quant Ultra"
VERSION = "1.0.0"

BROKER_NAME = "UPSTOX"

PAPER_TRADING = True
LIVE_TRADING = False

# =========================================================
# SYMBOL
# =========================================================

EXCHANGE = "NSE"

SYMBOL_NAME = "INFY"

TIMEFRAME = "5minute"

# =========================================================
# STRATEGY
# =========================================================

STRATEGY_NAME = "EMA_RSI_VWAP"

EMA_FAST = 20
EMA_SLOW = 50

RSI_PERIOD = 14
ATR_PERIOD = 14

VWAP_ENABLED = True

# =========================================================
# SIGNAL RULES
# =========================================================

BUY_RSI = 55
SELL_RSI = 45

BUY_CONFIDENCE = 70
SELL_CONFIDENCE = 70

# =========================================================
# RISK MANAGEMENT
# =========================================================

DEFAULT_RISK_PERCENT = 1.0

RISK_REWARD_RATIO = 2.0

MAX_OPEN_TRADES = 5

MAX_CAPITAL_PER_TRADE = 0.20      # 20%

MAX_DAILY_LOSS_PERCENT = 3.0

# =========================================================
# COST ENGINE
# =========================================================

BROKERAGE_PER_ORDER = 20.0

INCLUDE_STT = True
INCLUDE_GST = True
INCLUDE_SEBI = True
INCLUDE_STAMP_DUTY = True

MIN_EXPECTED_NET_PROFIT = 150.0

# =========================================================
# MARGIN
# =========================================================

DEFAULT_MARGIN_PERCENT = 20

# =========================================================
# TELEGRAM
# =========================================================

TELEGRAM_ENABLED = False

# =========================================================
# GUARDIAN AI
# =========================================================

NEWS_FILTER = True
SENTIMENT_FILTER = True
VIX_FILTER = True
EVENT_FILTER = True

MIN_GUARDIAN_SCORE = 70

# =========================================================
# PAPER TRADING
# =========================================================

SAVE_TRADES = True

# =========================================================
# JOURNAL
# =========================================================

JOURNAL_FILE = "journal/trades.csv"

# =========================================================
# REPORTS
# =========================================================

REPORTS_FOLDER = "reports"

# =========================================================
# LOGGING
# =========================================================

LOG_LEVEL = "INFO"

# =========================================================
# MARKET HOURS
# =========================================================

MARKET_OPEN = "09:15"

MARKET_CLOSE = "15:30"

# =========================================================
# COLORS
# =========================================================

SUCCESS = "🟢"

WARNING = "🟡"

ERROR = "🔴"

INFO = "🔵"

# =========================================================
# TRAILING STOP
# =========================================================

ATR_TRAILING_MULTIPLIER = 1.5

BREAK_EVEN_TRIGGER = 1.0

PARTIAL_BOOKING_PERCENT = 50

# =====================================================
# PARTIAL EXIT
# =====================================================

PARTIAL_BOOKING_PERCENT = 50

ENABLE_PARTIAL_EXIT = True

# =========================================================
# DAILY RISK GUARD
# =========================================================

MAX_DAILY_LOSS_PERCENT = 3

MAX_DAILY_PROFIT_PERCENT = 5

MAX_CONSECUTIVE_LOSSES = 3

# =====================================================
# MARKET SESSION
# =====================================================

MARKET_START_HOUR = 9
MARKET_START_MINUTE = 20

MARKET_END_HOUR = 15
MARKET_END_MINUTE = 20

AUTO_EXIT_TIME = "15:25"

ENABLE_AUTO_SCHEDULER = True

# =========================================================
# INDIA VIX
# =========================================================

ENABLE_VIX_FILTER = True

MAX_VIX_ALLOWED = 30

LOW_VIX = 12

NORMAL_VIX = 20

HIGH_VIX = 25

# =========================================================
# ECONOMIC CALENDAR
# =========================================================

ENABLE_ECONOMIC_FILTER = True

EVENT_LOOKAHEAD_MINUTES = 60

BLOCK_HIGH_IMPACT_EVENTS = True

# =====================================================
# FII / DII
# =====================================================

ENABLE_FII_DII_FILTER = True

FII_WEIGHT = 25

DII_WEIGHT = 10

# =====================================================
# GIFT NIFTY
# =====================================================

ENABLE_GIFT_NIFTY = True

GAP_UP_THRESHOLD = 0.30

STRONG_GAP_THRESHOLD = 1.00

# =====================================================
# GLOBAL MARKET FILTER
# =====================================================

ENABLE_GLOBAL_MARKET = True

GLOBAL_MARKET_WEIGHT = 15

# =====================================================
# LIVE TRADING
# =====================================================

LIVE_TRADING = False

PAPER_TRADING = True