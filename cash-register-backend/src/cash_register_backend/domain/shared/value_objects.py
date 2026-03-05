from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID, uuid4


@dataclass
class EntityId:
    value: UUID

    @classmethod
    def generate(cls) -> "EntityId":
        return cls(value=uuid4())

    @classmethod
    def from_string(cls, value: str) -> "EntityId":
        return cls(value=UUID(value))


@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __post_init__(self) -> None:
        if self.amount < Decimal("0"):
            raise ValueError("Money amount cannot be negative")

    def __add__(self, other: "Money") -> "Money":
        return Money(
            amount=self.amount + other.amount,
            currency=self.currency,
        )

    def __sub__(self, other: "Money") -> "Money":
        return Money(
            amount=self.amount - other.amount,
            currency=self.currency,
        )
