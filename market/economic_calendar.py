"""
=========================================================
QUANT ULTRA
Economic Calendar Engine
=========================================================
"""

from datetime import datetime


class EconomicCalendar:

    def __init__(self):

        self.events = []

    # -------------------------------------------------

    def load(self, events):

        """
        events = [

            {

                "time":"2026-08-05 14:30",

                "event":"RBI Policy",

                "impact":"HIGH"

            }

        ]
        """

        self.events = events

    # -------------------------------------------------

    def upcoming(self, within_minutes=60):

        now = datetime.now()

        upcoming = []

        for event in self.events:

            event_time = datetime.strptime(

                event["time"],

                "%Y-%m-%d %H:%M",

            )

            diff = (

                event_time - now

            ).total_seconds() / 60

            if 0 <= diff <= within_minutes:

                upcoming.append(event)

        return upcoming

    # -------------------------------------------------

    def should_trade(self):

        events = self.upcoming()

        for event in events:

            if event["impact"] == "HIGH":

                return {

                    "allowed": False,

                    "reason": event["event"],

                }

        return {

            "allowed": True,

            "reason": None,

        }

    # -------------------------------------------------

    def dashboard(self):

        print()

        print("=" * 60)

        print("📅 ECONOMIC CALENDAR")

        print("=" * 60)

        upcoming = self.upcoming()

        if not upcoming:

            print("No important events.")

        else:

            for event in upcoming:

                print(

                    f"{event['time']} | "

                    f"{event['impact']} | "

                    f"{event['event']}"

                )

        print("=" * 60)


# ---------------------------------------------------------

if __name__ == "__main__":

    calendar = EconomicCalendar()

    calendar.load(

        [

            {

                "time":"2026-08-05 14:30",

                "event":"RBI Policy",

                "impact":"HIGH",

            },

            {

                "time":"2026-08-05 16:00",

                "event":"GDP",

                "impact":"MEDIUM",

            },

        ]

    )

    calendar.dashboard()

    print()

    print(calendar.should_trade())