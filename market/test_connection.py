from dotenv import load_dotenv
import os
import upstox_client
from pprint import pprint

load_dotenv()

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)
market_api = upstox_client.MarketQuoteApi(api_client)

try:
    response = market_api.get_full_market_quote(
        "NSE_EQ|INE009A01021",
        "2.0"
    )

    print("🎉 SUCCESS!")
    pprint(response)

except Exception as e:
    print("❌ ERROR")
    print(e)