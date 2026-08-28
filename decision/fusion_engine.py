"""
=========================================================
QUANT ULTRA
Decision Fusion Engine
=========================================================
Combines recommendations from all engines.
=========================================================
"""


class DecisionFusionEngine:

    def evaluate(

        self,

        decisions,

    ):

        result = {

            "action": "HOLD",

            "confidence": 100,

            "reasons": [],

        }

        # -----------------------------------------
        # Highest Priority : EXIT
        # -----------------------------------------

        for decision in decisions:

            if decision["action"] == "EXIT":

                return {

                    "action": "EXIT",

                    "confidence": decision["confidence"],

                    "reasons": [

                        decision["reason"]

                    ],

                }

        # -----------------------------------------
        # Partial Exit
        # -----------------------------------------

        for decision in decisions:

            if decision["action"] == "PARTIAL_EXIT":

                result = {

                    "action": "PARTIAL_EXIT",

                    "confidence": decision["confidence"],

                    "reasons": [

                        decision["reason"]

                    ],

                }

        # -----------------------------------------
        # Trailing Stop
        # -----------------------------------------

        for decision in decisions:

            if decision["action"] == "TRAIL":

                result = {

                    "action": "TRAIL",

                    "confidence": decision["confidence"],

                    "reasons": [

                        decision["reason"]

                    ],

                }

        return result


if __name__ == "__main__":

    print()

    print("=" * 60)

    print("DECISION FUSION ENGINE READY")

    print("=" * 60)