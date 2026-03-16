from dataclasses import dataclass, field
from datetime import datetime, UTC
from decimal import Decimal

from cash_register_backend.domain.product import Product
from cash_register_backend.domain.product.enums import ProductType
from cash_register_backend.domain.receipt import Discount
from cash_register_backend.domain.receipt.enums import ReceiptStatus
from cash_register_backend.domain.receipt.exceptions import (
    ProductIsInactiveForSaleException,
    InsufficientStockForReceiptException,
    ReceiptCannotBeRefundedException,
)
from cash_register_backend.domain.shared import EntityId, Money


@dataclass
class ReceiptItem:
    id: EntityId
    product_id: EntityId
    product_name: str
    product_price: Money
    quantity: Decimal

    @property
    def subtotal(self) -> Money:
        return Money(self.product_price.amount * self.quantity)


@dataclass
class Receipt:
    id: EntityId
    cashier_id: EntityId
    closed_at: datetime
    status: ReceiptStatus = ReceiptStatus.PAID
    items: list[ReceiptItem] = field(default_factory=list)
    discount: Discount | None = None
    created_at: datetime = field(default=datetime.now(UTC))

    def add_item(self, product: Product, quantity: Decimal) -> None:
        if not product.is_active:
            raise ProductIsInactiveForSaleException()
        if (
            not product.product_type.value == ProductType.SERVICE
            and product.stock
            and not product.stock.is_sufficient(quantity)
        ):
            raise InsufficientStockForReceiptException()

        #  Если товар уже в чеке
        for item in self.items:
            if item.product_name == product.name:
                item.quantity += quantity
                return

        self.items.append(
            ReceiptItem(
                id=EntityId.generate(),
                product_id=product.id,
                product_name=product.name,
                product_price=product.price,
                quantity=quantity,
            )
        )

    def remove_item(self, product_id: EntityId) -> None:
        self.items = [item for item in self.items if item.product_id != product_id]

    def apply_discount(self, discount: Discount) -> None:
        self.discount = discount

    def cancel(self) -> None:
        self.status = ReceiptStatus.CANCELLED
        self.closed_at = datetime.now(UTC)

    def close(self) -> None:
        """Если оплата успешно прошла"""
        self.status = ReceiptStatus.PAID
        self.closed_at = datetime.now(UTC)

    def refund(self) -> None:
        if self.status != ReceiptStatus.PAID:
            raise ReceiptCannotBeRefundedException()
        self.status = ReceiptStatus.REFUNDED
        self.closed_at = datetime.now(UTC)

    @property
    def total(self) -> Money:
        if not self.items:
            return Money(Decimal("0"))
        total_ = Decimal(sum(item.subtotal.amount for item in self.items))
        if self.discount:
            total_ = self.discount.apply_to(total_)
        return Money(total_)
