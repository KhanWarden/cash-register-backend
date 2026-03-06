from abc import ABC, abstractmethod

from cash_register_backend.domain.shared import EntityId
from cash_register_backend.domain.product import Product, StockKeepingUnit, Barcode


class IProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, product_id: EntityId) -> Product | None:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Product | list[Product] | None:
        pass

    @abstractmethod
    def get_by_sku(self, sku: StockKeepingUnit) -> Product | None:
        pass

    @abstractmethod
    def get_by_barcode(self, barcode: Barcode) -> Product | None:
        pass

    @abstractmethod
    def get_all_active(self) -> list[Product]:
        pass

    @abstractmethod
    def save(self, product: Product) -> None:
        pass
