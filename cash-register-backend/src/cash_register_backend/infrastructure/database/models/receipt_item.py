from typing import TYPE_CHECKING
from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import mapped_column, Mapped, relationship

from cash_register_backend.infrastructure.database.models import Base

if TYPE_CHECKING:
    from cash_register_backend.infrastructure.database.models import ReceiptORM


class ReceiptItemORM(Base):
    __tablename__ = "receipt_items"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    receipt_id: Mapped[UUID] = mapped_column(ForeignKey("receipts.id"))
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"))
    product_name: Mapped[str]
    product_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 3))

    receipt: Mapped["ReceiptORM"] = relationship(back_populates="items")
