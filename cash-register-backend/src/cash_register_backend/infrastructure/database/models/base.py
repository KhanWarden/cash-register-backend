from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)
from cash_register_backend.core.utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        tablename = cls.__name__.replace("ORM", "")
        return f"{camel_case_to_snake_case(tablename)}s".lower()
