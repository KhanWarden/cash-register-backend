from typing import TYPE_CHECKING

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cash_register_backend.core.config import settings

if TYPE_CHECKING:
    from typing import Generator
    from sqlalchemy import Engine
    from sqlalchemy.orm import Session


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
    ) -> None:
        self.engine: Engine = create_engine(
            url=url,
            echo=echo,
        )
        self.session_factory: sessionmaker[Session] = sessionmaker(
            bind=self.engine,
        )

    def session_getter(self) -> "Generator[Session, None, None]":
        session = self.session_factory()
        try:
            yield session
        finally:
            session.close()


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
)
