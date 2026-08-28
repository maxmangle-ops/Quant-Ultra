"""
=========================================================
QUANT ULTRA
Upstox Live Order Engine
=========================================================
"""

import os

import upstox_client

from dotenv import load_dotenv

load_dotenv()


class UpstoxOrderEngine:

    def __init__(self):

        configuration = upstox_client.Configuration()

        configuration.access_token = os.getenv(
            "UPSTOX_ACCESS_TOKEN"
        )

        self.client = upstox_client.ApiClient(
            configuration
        )

        self.api = upstox_client.OrderApi(
            self.client
        )

    # -------------------------------------------------
    # Place Order
    # -------------------------------------------------

    def place_order(

        self,

        instrument_key,

        quantity,

        side,

        order_type="MARKET",

        product="I",

        price=None,

        trigger_price=None,

    ):

        try:

            order = {

                "quantity": quantity,

                "product": product,

                "validity": "DAY",

                "price": price,

                "tag": "QUANT_ULTRA",

                "instrument_token": instrument_key,

                "order_type": order_type,

                "transaction_type": side,

                "disclosed_quantity": 0,

                "trigger_price": trigger_price,

                "is_amo": False,

            }

            response = self.api.place_order(order)

            return {

                "success": True,

                "response": response,

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e),

            }

    # -------------------------------------------------
    # Cancel
    # -------------------------------------------------

    def cancel_order(

        self,

        order_id,

    ):

        try:

            response = self.api.cancel_order(

                order_id

            )

            return {

                "success": True,

                "response": response,

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e),

            }

    # -------------------------------------------------
    # Modify
    # -------------------------------------------------

    def modify_order(

        self,

        order_id,

        quantity=None,

        price=None,

        trigger_price=None,

    ):

        try:

            response = self.api.modify_order(

                order_id=order_id,

                quantity=quantity,

                price=price,

                trigger_price=trigger_price,

            )

            return {

                "success": True,

                "response": response,

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e),

            }

    # -------------------------------------------------
    # Order History
    # -------------------------------------------------

    def history(

        self,

        order_id,

    ):

        try:

            return self.api.get_order_details(

                order_id

            )

        except Exception as e:

            print(e)

            return None


# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("🚀 UPSTOX ORDER ENGINE READY")

    print("=" * 60)

    print()

    print("⚠ Live order placement disabled in test mode.")