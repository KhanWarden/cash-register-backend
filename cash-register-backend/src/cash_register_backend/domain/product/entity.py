from dataclasses import dataclass

from cash_register_backend.domain.product import StockKeepingUnit
from cash_register_backend.domain.product.enums import ProductType, MeasurementUnit
from cash_register_backend.domain.shared import EntityId, Money


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
