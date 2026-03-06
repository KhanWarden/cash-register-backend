from abc import ABC, abstractmethod

from cash_register_backend.domain.payment import Payment
from cash_register_backend.domain.shared import EntityId


class IPaymentRepository(ABC):
    @abstractmethod
    def get_by_receipt_id(self, receipt_id: EntityId) -> list[Payment]:
        pass

    @abstractmethod
    def save(self, payment: Payment) -> None:
        pass
