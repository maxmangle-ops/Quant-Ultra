import os

import upstox_client
from dotenv import load_dotenv

load_dotenv()

configuration = upstox_client.Configuration()

configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

client = upstox_client.ApiClient(configuration)

api = upstox_client.MarketQuoteApi(client)

print("=" * 70)
print("OPTION LTP TEST")
print("=" * 70)

instrument = "NSE_FO|63949"

response = api.ltp(

    symbol=instrument,

    api_version="2.0",

)

print(response)