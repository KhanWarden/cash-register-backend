from sqlalchemy.orm import Session

from cash_register_backend.domain.shared import EntityId
from cash_register_backend.domain.user import (
    IUserRepository,
    User,
    Username,
    HashedPassword,
)
from cash_register_backend.domain.user.enums import UserRole
from cash_register_backend.infrastructure.database.models import User as UserModel


class UserRepository(IUserRepository):
    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    def get_by_id(self, user_id: EntityId) -> User | None:
        user = self._session.get(UserModel, user_id.value)
        if user is None:
            return None
        return self._to_entity(user)

    def save(self, user: User) -> None:
        model = self._to_model(user)
        self._session.add(model)
        self._session.commit()

    def get_by_username(self, username: str) -> User | None:
        user = self._session.get(UserModel, username)
        if user is None:
            return None
        return self._to_entity(user)

    @staticmethod
    def _to_model(user: User) -> User:
        return UserModel(
            id=user.id.value,
            username=user.username.value,
            first_name=user.first_name,
            role=user.role.value,
            hashed_password=user.hashed_password.value,
            is_active=user.is_active,
            created_at=user.created_at,
        )

    @staticmethod
    def _to_entity(user_model: UserModel) -> User:
        return User(
            id=EntityId(user_model.id),
            username=Username(user_model.username),
            first_name=user_model.first_name,
            last_name=user_model.last_name,
            role=UserRole(user_model.role),
            hashed_password=HashedPassword(user_model.hashed_password),
            is_active=user_model.is_active,
            created_at=user_model.created_at,
        )
