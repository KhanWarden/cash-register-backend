from enum import Enum


class PaymentMethod(str, Enum):
    CASH = "cash"
    CARD = "card"
    MIXED = "mixed"
