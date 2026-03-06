from typing import TYPE_CHECKING
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import (
    String,
    Numeric,
    ForeignKey,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from cash_register_backend.infrastructure.database.models import Base

if TYPE_CHECKING:
    from .category import Category


class Product(Base):
    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    product_type: Mapped[str] = mapped_column(String(30))
    unit: Mapped[str] = mapped_column(String(10))
    price: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    sku: Mapped[str] = mapped_column(String(50), unique=True)
    category_id: Mapped[UUID] = mapped_column(ForeignKey("categories.id"))
    barcode: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
    )
    is_active: Mapped[bool] = mapped_column(Boolean)
    stock_quantity: Mapped[Decimal | None] = mapped_column(
        Numeric(precision=10, scale=3),
    )
    created_at: Mapped[datetime] = mapped_column(DateTime)

    categories: Mapped["Category"] = relationship(back_populates="categories")
