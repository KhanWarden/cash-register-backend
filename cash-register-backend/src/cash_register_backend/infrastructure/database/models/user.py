from uuid import UUID
from datetime import datetime

from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from cash_register_backend.infrastructure.database.models import Base


class User(Base):
    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    role: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
