from sqlalchemy import select
from sqlalchemy.orm import Session

from cash_register_backend.domain.category import ICategoryRepository, Category
from cash_register_backend.domain.shared import EntityId
from cash_register_backend.infrastructure.database.models import (
    Category as CategoryModel,
)


class CategoryRepository(ICategoryRepository):
    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    def get_by_id(self, category_id: EntityId) -> Category | None:
        result = self._session.get(CategoryModel, category_id.value)
        if result is None:
            return None
        return self._to_entity(result)

    def get_all_active(self) -> list[Category]:
        result = self._session.execute(
            select(CategoryModel).where(CategoryModel.is_active.is_(True))
        )
        return [self._to_entity(row) for row in result.scalars().all()]

    def save(self, category: Category) -> None:
        result = self._session.get(CategoryModel, category.id.value)
        if result is None:
            self._session.add(self._to_model(category))
        else:
            result.name = category.name
            result.is_active = category.is_active
        self._session.flush()

    def exists_by_name(self, name: str) -> bool:
        result = self._session.execute(
            select(CategoryModel).where(CategoryModel.name.is_(name))
        )
        return result.scalar_one_or_none() is not None

    @staticmethod
    def _to_entity(model: CategoryModel) -> Category:
        return Category(
            id=EntityId(model.id),
            name=model.name,
            is_active=model.is_active,
            created_at=model.created_at,
        )

    @staticmethod
    def _to_model(category: Category) -> CategoryModel:
        return CategoryModel(
            id=category.id.value,
            name=category.name,
            is_active=category.is_active,
            created_at=category.created_at,
        )
