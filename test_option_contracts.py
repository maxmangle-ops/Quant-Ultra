import os
from dotenv import load_dotenv
import upstox_client

load_dotenv()

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

client = upstox_client.ApiClient(configuration)
api = upstox_client.OptionsApi(client)

print("=" * 80)
print("REQUESTING OPTION CONTRACTS")
print("=" * 80)

response = api.get_option_contracts(
    instrument_key="NSE_INDEX|Nifty 50"
)

print("\nStatus:")
print(response.status)

print("\nResponse Type:")
print(type(response.data))

print("\nLength:")

try:
    print(len(response.data))
except Exception as e:
    print(e)

print("\nFirst Item:")

try:
    print(response.data[0])
except Exception as e:
    print(e)

print("\nData Attributes:")

try:
    print(dir(response.data[0]))
except Exception as e:
    print(e)