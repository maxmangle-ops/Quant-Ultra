"""
=========================================================
QUANT ULTRA
Multi Symbol Scanner
=========================================================
"""

from engine.live_analyzer import analyze


class MultiSymbolScanner:

    def __init__(self, symbols):

        self.symbols = symbols

    # -------------------------------------------------

    def scan(self):

        results = []

        print()
        print("=" * 60)
        print("🔍 SCANNING MARKET")
        print("=" * 60)

        for symbol in self.symbols:

            try:

                analysis = analyze(symbol)

                analysis.symbol = symbol

                results.append(analysis)

                print(
                    f"{symbol:15}"
                    f" Score={analysis.technical_score:3}"
                    f" Trend={analysis.trend}"
                )

            except Exception as e:

                print(f"{symbol}: {e}")

        return results

    # -------------------------------------------------

    def best_trade(self):

        results = self.scan()

        if not results:

            return None

        results.sort(

            key=lambda x: x.technical_score,

            reverse=True,

        )

        best = results[0]

        print()

        print("=" * 60)
        print("🏆 BEST OPPORTUNITY")
        print("=" * 60)

        print(f"Symbol : {best.symbol}")
        print(f"Score  : {best.technical_score}")
        print(f"Trend  : {best.trend}")

        print("=" * 60)

        return best


# ---------------------------------------------------------

if __name__ == "__main__":

    scanner = MultiSymbolScanner(

        [

            "NIFTY",

            "BANKNIFTY",

            "SENSEX",

        ]

    )

    scanner.best_trade()
