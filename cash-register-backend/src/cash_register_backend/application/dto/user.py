from uuid import UUID
from pydantic import BaseModel, field_validator

from cash_register_backend.domain.user.enums import UserRole


class CreateUserDTO(BaseModel):
    username: str
    first_name: str
    last_name: str
    role: UserRole
    plain_password: str

    @field_validator("username")
    @classmethod
    def username_must_be_valid(cls, value: str) -> str:
        if len(value.strip()) < 2:
            raise ValueError("Username must be at least 2 characters long")
        return value.strip()

    @field_validator("plain_password")
    @classmethod
    def password_must_be_strong(cls, value: str) -> str:
        if len(value) < 4:
            raise ValueError("Password must be at least 4 characters long")
        return value


class LoginDTO(BaseModel):
    username: str
    plain_password: str


class ChangeRoleDTO(BaseModel):
    user_id: UUID
    changed_by_id: UUID
    new_role: UserRole


class ActivateUserDTO(BaseModel):
    user_id: UUID
    changed_by_id: UUID


class DeactivateUserDTO(BaseModel):
    user_id: UUID
    changed_by_id: UUID
