from dataclasses import dataclass, field
from datetime import datetime, UTC

from cash_register_backend.domain.shared import EntityId
from cash_register_backend.domain.user import HashedPassword
from cash_register_backend.domain.user.enums import UserRole
from cash_register_backend.domain.user.exceptions import (
    CannotDeactivateAdminException,
    InactiveUserException,
)


@dataclass
class User:
    id: EntityId
    username: str
    first_name: str
    last_name: str
    role: UserRole
    hashed_password: HashedPassword
    is_active: bool = True
    created_at: datetime = field(default=datetime.now(UTC))

    def deactivate(self) -> None:
        if self.role == UserRole.ADMIN:
            raise CannotDeactivateAdminException(self.id)
        self.is_active = False

    def activate(self) -> None:
        self.is_active = True

    def change_role(self, new_role: UserRole) -> None:
        if not self.is_active:
            raise InactiveUserException(self.id)
        self.role = new_role
