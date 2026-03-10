from abc import ABC, abstractmethod

from cash_register_backend.domain.payment import Payment
from cash_register_backend.domain.shared import EntityId


class IPaymentRepository(ABC):
    @abstractmethod
    def get_by_payment_id(self, payment_id: EntityId) -> Payment | None:
        pass

    @abstractmethod
    def get_by_receipt_id(self, receipt_id: EntityId) -> list[Payment] | None:
        pass

    @abstractmethod
    def get_by_cashier_id(self, receipt_id: EntityId) -> list[Payment] | None:
        pass

    @abstractmethod
    def save(self, payment: Payment) -> None:
        pass
