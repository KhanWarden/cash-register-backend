from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Discount:
    value: Decimal

    def __post_init__(self) -> None:
        if not (Decimal("0") < self.value <= Decimal("1")):
            raise ValueError("Discount must be between 0 and 1")

    def apply_to(self, amount: Decimal) -> Decimal:
        return amount * (Decimal("1") - self.value)
