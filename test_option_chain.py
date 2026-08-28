import os
from dotenv import load_dotenv
import upstox_client

load_dotenv()

configuration = upstox_client.Configuration()
configuration.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

api_client = upstox_client.ApiClient(configuration)

print("SDK Loaded Successfully")

print("\nAvailable API Classes:\n")

for name in dir(upstox_client):
    if name.endswith("Api"):
        print(name)