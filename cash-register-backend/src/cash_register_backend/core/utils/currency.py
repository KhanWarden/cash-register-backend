from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cash_register_backend.core.config.currency_enum import Currency


def get_default_currency() -> "Currency":
    from cash_register_backend.core.config import settings

    return settings.app.currency
