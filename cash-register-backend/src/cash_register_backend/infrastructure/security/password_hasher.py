from passlib.context import CryptContext

from cash_register_backend.application.services import IPasswordService


class BcryptPasswordService(IPasswordService):
    def __init__(self) -> None:
        self._context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(
        self,
        plain_password: str,
    ) -> str:
        return self._context.hash(plain_password)

    def verify(
        self,
        plain_password: str,
        hashed_password: str,
    ) -> bool:
        return self._context.verify(plain_password, hashed_password)
