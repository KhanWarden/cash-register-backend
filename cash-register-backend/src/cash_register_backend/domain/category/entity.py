from dataclasses import dataclass, field
from datetime import datetime, UTC

from cash_register_backend.domain.shared import EntityId


@dataclass
class Category:
    id: EntityId
    name: str
    description: str | None = None
    is_active: bool = True
    created_at: datetime = field(default=datetime.now(UTC))

    def activate(self) -> None:
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False
