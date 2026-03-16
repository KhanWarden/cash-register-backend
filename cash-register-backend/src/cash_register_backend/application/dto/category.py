from uuid import UUID

from pydantic import BaseModel, field_validator


class CreateCategoryDTO(BaseModel):
    name: str


class UpdateCategoryDTO(BaseModel):
    id: UUID
    name: str

    @field_validator("name")
    @classmethod
    def name_must_be_valid(cls, value: str) -> str:
        if len(value.strip()) < 2:
            raise ValueError("Category name is too short")
        return value.strip()


class ActivateCategoryDTO(BaseModel):
    id: UUID


class DeactivateCategoryDTO(BaseModel):
    id: UUID
