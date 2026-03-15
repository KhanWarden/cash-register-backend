from cash_register_backend.application.dto import (
    CreateCategoryDTO,
    UpdateCategoryDTO,
    DeactivateCategoryDTO,
)
from cash_register_backend.domain.category import ICategoryRepository, Category
from cash_register_backend.domain.category.exceptions import (
    DuplicateCategoryNameException,
    CategoryNotFoundException,
)
from cash_register_backend.domain.shared import EntityId


class CreateCategoryUseCase:
    def __init__(
        self,
        category_repository: ICategoryRepository,
    ) -> None:
        self._categories = category_repository

    def execute(self, dto: CreateCategoryDTO) -> Category:
        if self._categories.exists_by_name(dto.name):
            raise DuplicateCategoryNameException()

        category = Category(
            id=EntityId.generate(),
            name=dto.name,
        )
        self._categories.save(category)
        return category


class UpdateCategoryUseCase:
    def __init__(
        self,
        category_repository: ICategoryRepository,
    ) -> None:
        self._categories = category_repository

    def execute(self, dto: UpdateCategoryDTO) -> Category:
        category = self._categories.get_by_id(EntityId(dto.id))
        if category is None:
            raise CategoryNotFoundException()

        if self._categories.exists_by_name(dto.name):
            raise DuplicateCategoryNameException()

        category.name = dto.name
        self._categories.save(category)
        return category


class DeactivateCategoryUseCase:
    def __init__(
        self,
        category_repository: ICategoryRepository,
    ) -> None:
        self._categories = category_repository

    def execute(self, dto: DeactivateCategoryDTO) -> None:
        category = self._categories.get_by_id(EntityId(dto.id))
        if category is None:
            raise CategoryNotFoundException()

        category.deactivate()
        self._categories.save(category)
