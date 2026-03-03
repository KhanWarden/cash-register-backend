from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from cash_register_backend.core.config.app import AppConfig
from cash_register_backend.core.config.database import DatabaseConfig
from cash_register_backend.core.config.logging import LoggingConfig


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CASH_REGISTER__",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    app: AppConfig = AppConfig()
    db: DatabaseConfig
    logging: LoggingConfig = LoggingConfig()


settings = Settings()
