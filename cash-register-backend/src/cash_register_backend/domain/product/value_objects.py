from dataclasses import dataclass


@dataclass(frozen=True)
class StockKeepingUnit:
    value: str

    def __post_init__(self) -> None:
        if not self.value or len(self.value) < 1:
            raise ValueError("SKU cannot be empty")
        if len(self.value) > 50:
            raise ValueError("SKU cannot be more than 50 digits")


@dataclass(frozen=True)
class Barcode:
    value: str

    def __post_init__(self) -> None:
        if not self.value.isdigit():
            raise ValueError("Barcode must contain only digits")
