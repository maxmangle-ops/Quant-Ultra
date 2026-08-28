"""
=========================================================
QUANT ULTRA
Telegram Notification Engine
=========================================================
"""

import os
import requests

from dotenv import load_dotenv

load_dotenv()


class TelegramBot:

    def __init__(self):

        self.token = os.getenv("TELEGRAM_BOT_TOKEN")

        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

    # -------------------------------------------------

    def send(self, message):

        if not self.token or not self.chat_id:

            print("⚠ Telegram credentials missing.")

            return False

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        payload = {

            "chat_id": self.chat_id,

            "text": message,

            "parse_mode": "Markdown"

        }

        try:

            response = requests.post(
                url,
                json=payload,
                timeout=10,
            )

            return response.status_code == 200

        except Exception as e:

            print(e)

            return False

    # -------------------------------------------------

    def trade_alert(

        self,

        symbol,

        side,

        entry,

        stop_loss,

        target,

        quantity,

    ):

        message = f"""
🚀 *QUANT ULTRA*

Trade Generated

📈 Symbol : {symbol}

📊 Side : {side}

💰 Entry : ₹{entry}

🛑 Stop Loss : ₹{stop_loss}

🎯 Target : ₹{target}

📦 Qty : {quantity}
"""

        self.send(message)

    # -------------------------------------------------

    def exit_alert(

        self,

        symbol,

        pnl,

        reason,

    ):

        message = f"""
✅ *TRADE CLOSED*

📈 Symbol : {symbol}

💵 P&L : ₹{pnl}

📌 Reason : {reason}
"""

        self.send(message)

    # -------------------------------------------------

    def error(self, text):

        self.send(f"❌ ERROR\n\n{text}")


# ---------------------------------------------------------

if __name__ == "__main__":

    bot = TelegramBot()

    bot.send("✅ Quant Ultra Telegram Connected")