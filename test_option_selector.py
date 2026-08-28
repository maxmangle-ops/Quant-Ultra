from market.option_chain import OptionChainEngine
from options.option_selector import OptionSelector

print("=" * 70)
print("OPTION SELECTOR TEST")
print("=" * 70)

chain = OptionChainEngine()

contracts = chain.get_contracts(
    "NSE_INDEX|Nifty 50"
)

selector = OptionSelector()

candidate = selector.select(

    contracts=contracts,

    spot_price=24239.5,

    trend="BULLISH",

    technical_score=70,

    underlying="NIFTY",

)

if candidate is None:

    print("No contract selected")

else:

    print()

    print("Selected Contract")

    print("----------------------------")

    print(candidate.contract.trading_symbol)

    print(candidate.contract.instrument_key)

    print(candidate.contract.strike)

    print(candidate.contract.option_type)

    print(candidate.contract.expiry)