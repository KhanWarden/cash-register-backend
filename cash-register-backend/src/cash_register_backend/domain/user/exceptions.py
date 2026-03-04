from typing import TYPE_CHECKING
from cash_register_backend.domain.shared import DomainException

if TYPE_CHECKING:
    from cash_register_backend.domain.shared import EntityId


class CannotDeactivateAdminException(DomainException):
    def __init__(self, user_id: EntityId):
        super().__init__(f"Admin {user_id} cannot be deactivated")


class InactiveUserException(DomainException):
    def __init__(self, user_id: EntityId):
        super().__init__(f"User {user_id} is not active")
