from dataclasses import dataclass, field
from datetime import datetime, UTC

from cash_register_backend.domain.receipt.enums import PaymentMethod
from cash_register_backend.domain.shared import EntityId, Money


@dataclass
class Payment:
    id: EntityId
    receipt_id: EntityId
    cashier_id: EntityId
    method: PaymentMethod
    amount: Money
    created_at: datetime = field(default=datetime.now(UTC))
