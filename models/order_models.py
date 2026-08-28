"""
=========================================================
QUANT ULTRA
Order Models
=========================================================
Canonical order object used throughout Quant Ultra.
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List


# =========================================================
# Order
# =========================================================

@dataclass
class Order:

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    order_id: str

    symbol: str

    side: str

    exchange: str

    # -----------------------------------------------------
    # Order Details
    # -----------------------------------------------------

    quantity: int

    order_type: str = "MARKET"

    product_type: str = "INTRADAY"

    price: float = 0.0

    trigger_price: float = 0.0

    # -----------------------------------------------------
    # Execution
    # -----------------------------------------------------

    status: str = "CREATED"

    filled_quantity: int = 0

    average_price: float = 0.0

    broker_order_id: Optional[str] = None

    broker_name: str = "PAPER"

    # -----------------------------------------------------
    # Trade Relation
    # -----------------------------------------------------

    position_id: Optional[int] = None

    parent_order: Optional[str] = None

    child_orders: List[str] = field(default_factory=list)

    # -----------------------------------------------------
    # Timing
    # -----------------------------------------------------

    created_at: datetime = field(default_factory=datetime.now)

    updated_at: datetime = field(default_factory=datetime.now)

    executed_at: Optional[datetime] = None

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    remarks: List[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    # =====================================================
    # Convenience Properties
    # =====================================================

    @property
    def is_open(self):

        return self.status.upper() in (

            "CREATED",

            "PENDING",

            "OPEN",

        )

    @property
    def is_filled(self):

        return self.status.upper() == "FILLED"

    @property
    def is_cancelled(self):

        return self.status.upper() == "CANCELLED"

    @property
    def is_rejected(self):

        return self.status.upper() == "REJECTED"

    # =====================================================
    # Helpers
    # =====================================================

    def add_remark(

        self,

        remark: str,

    ):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.remarks.append(

            f"{timestamp} {remark}"

        )

    # -----------------------------------------------------

    def mark_filled(

        self,

        average_price: float,

    ):

        self.status = "FILLED"

        self.average_price = average_price

        self.filled_quantity = self.quantity

        self.executed_at = datetime.now()

        self.updated_at = datetime.now()

        self.add_remark(

            "Order Filled"

        )

    # -----------------------------------------------------

    def mark_cancelled(self):

        self.status = "CANCELLED"

        self.updated_at = datetime.now()

        self.add_remark(

            "Order Cancelled"

        )

    # -----------------------------------------------------

    def mark_rejected(

        self,

        reason: str,

    ):

        self.status = "REJECTED"

        self.updated_at = datetime.now()

        self.add_remark(

            f"Rejected : {reason}"

        )

    # -----------------------------------------------------

    def to_dict(self):

        """
        Compatibility layer for legacy modules.
        """

        return self.__dict__.copy()


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    order = Order(

        order_id="ORD0001",

        symbol="NIFTY26JUL24250CE",

        side="BUY",

        exchange="NSE_FO",

        quantity=75,

    )

    order.mark_filled(

        average_price=126.45,

    )

    print()

    print("=" * 60)

    print("ORDER MODEL READY")

    print("=" * 60)

    print(order)