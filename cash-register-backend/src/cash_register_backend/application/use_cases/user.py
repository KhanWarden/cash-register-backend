from cash_register_backend.application.dto import (
    CreateUserDTO,
    LoginDTO,
    ChangeRoleDTO,
    DeactivateUserDTO,
    ActivateUserDTO,
)
from cash_register_backend.application.services import IPasswordService
from cash_register_backend.domain.shared import EntityId
from cash_register_backend.domain.user import (
    IUserRepository,
    User,
    HashedPassword,
    Username,
)
from cash_register_backend.domain.user.exceptions import (
    UserNotFoundException,
    InactiveUserException,
)


class CreateUserUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        password_service: IPasswordService,
    ) -> None:
        self._users = user_repository
        self._password_service = password_service

    def execute(self, dto: CreateUserDTO) -> User:
        if self._users.get_by_username(dto.username):
            raise ValueError("User with this username already exists")

        hashed = HashedPassword(self._password_service.hash(dto.plain_password))
        user = User(
            id=EntityId.generate(),
            username=Username(dto.username),
            hashed_password=hashed,
            first_name=dto.first_name,
            last_name=dto.last_name,
            role=dto.role,
        )
        self._users.save(user)
        return user


class LoginUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        password_service: IPasswordService,
    ) -> None:
        self._users = user_repository
        self._password_service = password_service

    def execute(self, dto: LoginDTO) -> bool:
        user = self._users.get_by_username(dto.username)
        if user is None:
            raise UserNotFoundException()

        if not user.is_active:
            raise InactiveUserException(user.id)

        if not self._password_service.verify(
            dto.plain_password, user.hashed_password.value
        ):
            raise ValueError("Incorrect password")

        return True


class ChangeRoleUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
    ) -> None:
        self._users = user_repository

    def execute(
        self,
        dto: ChangeRoleDTO,
    ) -> User:
        user = self._users.get_by_id(EntityId(dto.user_id))
        if user is None:
            raise UserNotFoundException()
        user.change_role(dto.new_role)
        self._users.save(user)
        return user


class DeactivateUserUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
    ) -> None:
        self._users = user_repository

    def execute(self, dto: DeactivateUserDTO) -> User:
        user = self._users.get_by_id(EntityId(dto.user_id))
        if user is None:
            raise UserNotFoundException()
        user.deactivate()
        self._users.save(user)
        return user


class ActivateUserUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
    ) -> None:
        self._users = user_repository

    def execute(self, dto: ActivateUserDTO) -> User:
        user = self._users.get_by_id(EntityId(dto.user_id))
        if user is None:
            raise UserNotFoundException()
        user.activate()
        self._users.save(user)
        return user
