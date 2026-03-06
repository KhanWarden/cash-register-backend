from sqlalchemy import select
from sqlalchemy.orm import Session

from cash_register_backend.domain.product import Product, Barcode, StockKeepingUnit
from cash_register_backend.domain.product.entity import ProductStock
from cash_register_backend.domain.product.enums import MeasurementUnit, ProductType
from cash_register_backend.domain.product.repository import IProductRepository
from cash_register_backend.domain.shared import EntityId, Money
from cash_register_backend.infrastructure.database.models import Product as ProductModel


class ProductRepository(IProductRepository):
    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    def get_by_id(self, product_id: EntityId) -> Product | None:
        result = self._session.get(ProductModel, product_id.value)
        if result is None:
            return None
        return self._to_entity(result)

    def get_by_name(self, name: str) -> list[Product] | None:
        result = self._session.execute(
            select(ProductModel).where(ProductModel.name.is_(name))
        )
        return [self._to_entity(row) for row in result.scalars().all()]

    def get_by_sku(self, sku: StockKeepingUnit) -> Product | None:
        result = self._session.execute(
            select(ProductModel).where(ProductModel.sku.is_(sku.value))
        )
        if result is None:
            return None
        return self._to_entity(result)

    def get_by_barcode(self, barcode: Barcode) -> Product | None:
        result = self._session.execute(
            select(ProductModel).where(ProductModel.barcode.is_(barcode.value))
        )
        if result is None:
            return None
        return self._to_entity(result)

    def get_all_active(self) -> list[Product]:
        result = self._session.execute(
            select(ProductModel).where(ProductModel.is_active.is_(True))
        )
        return [self._to_entity(row) for row in result.scalars().all()]

    def save(self, product: Product) -> None:
        model = self._session.get(ProductModel, product.id.value)
        if model is None:
            self._session.add(self._to_model(product))
        else:
            model.name = product.name
            model.product_type = product.product_type.value
            model.unit = product.unit.value
            model.price = product.price.amount
            model.sku = product.sku.value
            model.category_id = product.category_id.value
            model.stock = product.stock.quantity if product.stock else None
            model.barcode = product.barcode.value if product.barcode else None
            model.is_active = product.is_active
        self._session.flush()

    @staticmethod
    def _to_entity(model: ProductModel) -> Product:
        return Product(
            id=EntityId(model.id),
            name=model.name,
            product_type=ProductType(model.product_type),
            unit=MeasurementUnit(model.unit),
            price=Money(model.price),
            sku=StockKeepingUnit(model.sku),
            category_id=EntityId(model.category_id),
            stock=ProductStock(model.stock_quantity) if model.stock_quantity else None,
            barcode=Barcode(model.barcode) if model.barcode else None,
            is_active=model.is_active,
            created_at=model.created_at,
        )

    @staticmethod
    def _to_model(product: Product) -> ProductModel:
        return ProductModel(
            id=product.id.value,
            name=product.name,
            product_type=product.product_type.value,
            unit=product.unit.value,
            price=product.price.amount,
            sku=product.sku.value,
            category_id=product.category_id.value,
            barcode=product.barcode.value if product.barcode else None,
            is_active=product.is_active,
            stock_quantity=product.stock.quantity if product.stock else None,
            created_at=product.created_at,
        )
