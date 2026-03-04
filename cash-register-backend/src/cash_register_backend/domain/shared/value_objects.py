from dataclasses import dataclass
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
