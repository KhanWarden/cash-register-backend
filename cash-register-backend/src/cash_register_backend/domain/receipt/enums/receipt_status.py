from enum import Enum


class ReceiptStatus(str, Enum):
    PAID = "paid"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"
