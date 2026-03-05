from pydantic import BaseModel

from cash_register_backend.core.config.currency_enum import Currency


class AppConfig(BaseModel):
    title: str = "Cash Register Backend"
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False

    currency: Currency
