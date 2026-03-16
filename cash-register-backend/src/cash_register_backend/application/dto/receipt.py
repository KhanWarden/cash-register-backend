from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, field_validator


class ReceiptItemDTO(BaseModel):
    product_id: UUID
    quantity: Decimal

    @field_validator("quantity")
    @classmethod
    def quantity_must_be_postiive(cls, value: Decimal) -> Decimal:
        if value < Decimal("0"):
            raise ValueError("Quantity must be positive")
        return value


class CreateReceiptDTO(BaseModel):
    cashier_id: UUID
    items: list[ReceiptItemDTO]
    discount: Decimal | None = None

    @field_validator("items")
    @classmethod
    def items_must_not_be_empty(
        cls,
        value: list[ReceiptItemDTO],
    ) -> list[ReceiptItemDTO]:
        if not value:
            raise ValueError("Receipt must contain at least one item")
        return value

    @field_validator("discount")
    @classmethod
    def discount_must_be_valid(cls, value: Decimal | None) -> Decimal | None:
        if value is not None and not (Decimal("0") < value <= Decimal("1")):
            raise ValueError("Discount must be between 0 and 1")
        return value


class CancelReceiptDTO(BaseModel):
    receipt_id: UUID
    cashier_id: UUID


class RefundReceiptDTO(BaseModel):
    receipt_id: UUID
    cashier_id: UUID
