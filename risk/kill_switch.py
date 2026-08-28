"""
=========================================================
QUANT ULTRA
Kill Switch
=========================================================
Emergency trading shutdown.
=========================================================
"""

from datetime import datetime


class KillSwitch:

    def __init__(self):

        self.active = False

        self.reason = None

        self.time = None

    # -------------------------------------------------

    def activate(self, reason):

        self.active = True

        self.reason = reason

        self.time = datetime.now()

        print()

        print("=" * 60)

        print("🛑 QUANT ULTRA KILL SWITCH")

        print("=" * 60)

        print(f"Status : ACTIVE")

        print(f"Reason : {reason}")

        print(f"Time   : {self.time}")

        print("=" * 60)

    # -------------------------------------------------

    def deactivate(self):

        self.active = False

        self.reason = None

        self.time = None

        print()

        print("✅ Kill Switch Deactivated")

    # -------------------------------------------------

    def can_trade(self):

        return not self.active

    # -------------------------------------------------

    def status(self):

        return {

            "active": self.active,

            "reason": self.reason,

            "time": self.time,

        }


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    ks = KillSwitch()

    ks.activate(

        "Daily Loss Limit Reached"

    )

    print()

    print(ks.status())