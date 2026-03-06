from abc import ABC, abstractmethod

from cash_register_backend.domain.receipt.entity import Receipt
from cash_register_backend.domain.shared import EntityId


class IReceiptRepository(ABC):
    @abstractmethod
    def get_by_id(self, receipt_id: EntityId) -> Receipt | None:
        pass

    @abstractmethod
    def get_by_cashier(self, cashier_id: EntityId) -> list[Receipt] | None:
        pass

    @abstractmethod
    def save(self) -> None:
        pass
