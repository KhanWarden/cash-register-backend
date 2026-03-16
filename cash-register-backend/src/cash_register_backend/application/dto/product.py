from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, field_validator

from cash_register_backend.domain.product.enums import ProductType, MeasurementUnit


def validate_positive_price(value: Decimal | None) -> Decimal | None:
    if value is not None and value < Decimal("0"):
        raise ValueError("Price must be positive")
    return value


class CreateProductDTO(BaseModel):
    name: str
    product_type: ProductType
    unit: MeasurementUnit
    price: Decimal
    sku: str
    category_id: UUID
    stock_quantity: Decimal | None = None
    barcode: str | None = None

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value: Decimal) -> Decimal:
        return validate_positive_price(value)

    @field_validator("stock_quantity")
    @classmethod
    def stock_must_be_positive(cls, value: Decimal | None) -> Decimal | None:
        if value is not None and value <= Decimal("0"):
            raise ValueError("Stock quantity must be positive")
        return value


class UpdateProductDTO(BaseModel):
    product_id: UUID
    name: str | None = None
    price: Decimal | None = None
    category_id: UUID | None = None
    barcode: str | None = None

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value: Decimal | None) -> Decimal | None:
        return validate_positive_price(value)


class AddStockDTO(BaseModel):
    product_id: UUID
    quantity: Decimal

    @field_validator("quantity")
    @classmethod
    def quantity_must_be_positive(cls, value: Decimal) -> Decimal:
        if value < Decimal("0"):
            raise ValueError("Quantity must be positive")
        return value


class DeactivateProductDTO(BaseModel):
    product_id: UUID
