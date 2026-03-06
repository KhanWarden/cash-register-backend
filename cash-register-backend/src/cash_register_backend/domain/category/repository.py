from abc import ABC, abstractmethod

from cash_register_backend.domain.category import Category
from cash_register_backend.domain.shared import EntityId


class ICategoryRepository(ABC):
    @abstractmethod
    def get_by_id(self, category_id: EntityId) -> Category | None:
        pass

    @abstractmethod
    def save(self, category: Category) -> None:
        pass

    @abstractmethod
    def exists_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def get_all_active(self) -> list[Category]:
        pass
