from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from cash_register_backend.infrastructure.database.models import Base
from cash_register_backend.infrastructure.database.models.payment import PaymentORM
from cash_register_backend.infrastructure.database.models.receipt_item import (
    ReceiptItemORM,
)


class ReceiptORM(Base):
    id: Mapped[UUID] = mapped_column(primary_key=True)
    cashier_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str]
    discount: Mapped[Decimal | None] = mapped_column(Numeric(5, 4))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    closed_at: Mapped[datetime] = mapped_column(DateTime)

    items: Mapped[list["ReceiptItemORM"]] = relationship(
        back_populates="receipt",
        cascade="all, delete-orphan",
    )
    payments: Mapped[list["PaymentORM"]] = relationship(back_populates="receipt")
