from dataclasses import dataclass, field
from datetime import datetime, UTC
from decimal import Decimal

from cash_register_backend.domain.product import StockKeepingUnit, Barcode
from cash_register_backend.domain.product.enums import ProductType, MeasurementUnit
from cash_register_backend.domain.product.exceptions import (
    CannotAdjustStockForServiceException,
    CannotChangePriceToZeroException,
    InsufficientStockException,
)
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
    stock: ProductStock | None = None
    barcode: Barcode | None = None
    is_active: bool = True
    created_at: datetime = field(default=datetime.now(UTC))

    def __post_init__(self) -> None:
        if self.product_type == ProductType.SERVICE and self.stock is not None:
            raise CannotAdjustStockForServiceException()

    def change_price(self, new_price: Money) -> None:
        if new_price.amount <= Decimal("0"):
            raise CannotChangePriceToZeroException()
        self.price = new_price

    def add_stock(self, quantity: Decimal) -> None:
        if self.product_type.value == ProductType.SERVICE:
            raise CannotAdjustStockForServiceException()
        self.stock = ProductStock(self.stock.quantity + quantity)

    def deduct_stock(self, quantity: Decimal) -> None:
        if self.product_type.value == ProductType.SERVICE:
            raise CannotAdjustStockForServiceException()
        if not self.stock or not self.stock.is_sufficient(quantity):
            raise InsufficientStockException()
        self.stock = ProductStock(self.stock.quantity - quantity)

    def activate(self) -> None:
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False
