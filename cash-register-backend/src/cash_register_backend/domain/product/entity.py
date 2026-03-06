from dataclasses import dataclass
from decimal import Decimal

from cash_register_backend.domain.product import StockKeepingUnit
from cash_register_backend.domain.product.enums import ProductType, MeasurementUnit
from cash_register_backend.domain.shared import EntityId, Money


@dataclass
class ProductStock:
    quantity: Decimal

    def __post_init__(self) -> None:
        if self.quantity < Decimal("0"):
            raise ValueError("Quantity cannot be negative")

    def is_sufficient(self, requested: Decimal) -> bool:
        return self.quantity >= requested


@dataclass
class Product:
    id: EntityId
    name: str
    product_type: ProductType
    unit: MeasurementUnit
    price: Money
    sku: StockKeepingUnit
    category_id: EntityId
    is_active: bool = True
