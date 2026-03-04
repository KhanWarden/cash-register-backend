from abc import ABC, abstractmethod

from cash_register_backend.domain.shared import EntityId
from cash_register_backend.domain.user import User


class IUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: EntityId) -> User | None:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
