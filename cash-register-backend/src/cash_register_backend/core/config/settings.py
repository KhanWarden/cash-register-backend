from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from cash_register_backend.core.config.app import AppConfig
from cash_register_backend.core.config.database import DatabaseConfig
from cash_register_backend.core.config.logging import LoggingConfig


CONFIG_DIR = Path(__file__).resolve().parent
ENVS_DIR = CONFIG_DIR / "envs"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="CASH_REGISTER__",
        env_nested_delimiter="__",
        env_file=ENVS_DIR / ".env"
    )
    app: AppConfig
    db: DatabaseConfig
    logging: LoggingConfig = LoggingConfig()


settings = Settings()
