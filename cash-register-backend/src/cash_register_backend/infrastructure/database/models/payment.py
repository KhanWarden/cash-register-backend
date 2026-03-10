from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey, DateTime, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from cash_register_backend.infrastructure.database.models import Base
from cash_register_backend.infrastructure.database.models import ReceiptORM


class PaymentORM(Base):
    id: Mapped[UUID] = mapped_column(primary_key=True)
    receipt_id: Mapped[UUID] = mapped_column(ForeignKey("receipts.id"))
    cashier_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    method: Mapped[str]
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    is_active: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    receipt: Mapped["ReceiptORM"] = relationship(back_populates="payments")
