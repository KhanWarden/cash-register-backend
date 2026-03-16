from decimal import Decimal

from cash_register_backend.application.dto import (
    CreateProductDTO,
    UpdateProductDTO,
    DeactivateProductDTO,
    AddStockDTO,
)
from cash_register_backend.domain.category import ICategoryRepository
from cash_register_backend.domain.category.exceptions import CategoryNotFoundException
from cash_register_backend.domain.product import (
    IProductRepository,
    Product,
    StockKeepingUnit,
    Barcode,
)
from cash_register_backend.domain.product.entity import ProductStock
from cash_register_backend.domain.product.enums import ProductType
from cash_register_backend.domain.product.exceptions import (
    DuplicateSkuException,
    ProductNotFoundException,
)
from cash_register_backend.domain.shared import EntityId, Money


class CreateProductUseCase:
    def __init__(
        self,
        product_repository: IProductRepository,
        category_repository: ICategoryRepository,
    ) -> None:
        self._products = product_repository
        self._categories = category_repository

    def execute(self, dto: CreateProductDTO) -> Product:
        category = self._categories.get_by_id(EntityId(dto.category_id))
        if category is None:
            raise CategoryNotFoundException()

        if self._products.get_by_sku(StockKeepingUnit(dto.sku)) is not None:
            raise DuplicateSkuException()

        stock = None
        if dto.product_type != ProductType.SERVICE:
            stock = ProductStock(dto.stock_quantity or Decimal("0"))

        product = Product(
            id=EntityId.generate(),
            name=dto.name,
            product_type=dto.product_type,
            unit=dto.unit,
            price=Money(dto.price),
            sku=StockKeepingUnit(dto.sku),
            category_id=EntityId(dto.category_id),
            stock=stock,
            barcode=Barcode(dto.barcode) if dto.barcode else None,
        )
        self._products.save(product)
        return product


class UpdateProductUseCase:
    def __init__(
        self,
        product_repository: IProductRepository,
        category_repository: ICategoryRepository,
    ) -> None:
        self._products = product_repository
        self._categories = category_repository

    def execute(self, dto: UpdateProductDTO) -> Product:
        product = self._products.get_by_id(EntityId(dto.product_id))
        if product is None:
            raise ProductNotFoundException()

        if dto.name is not None:
            product.name = dto.name

        if dto.price is not None:
            product.price = Money(dto.price)

        if dto.barcode is not None:
            product.barcode = dto.barcode

        if dto.category_id is not None:
            category = self._categories.get_by_id(EntityId(dto.category_id))
            if category is None:
                raise CategoryNotFoundException()
            product.category_id = EntityId(dto.category_id)

        self._products.save(product)
        return product


class AddStockUseCase:
    def __init__(
        self,
        product_repository: IProductRepository,
    ) -> None:
        self._products = product_repository

    def execute(self, dto: AddStockDTO) -> Product:
        product = self._products.get_by_id(EntityId(dto.product_id))
        if product is None:
            raise ProductNotFoundException()

        product.add_stock(dto.quantity)
        self._products.save(product)
        return product


class DeactivateProductUseCase:
    def __init__(
        self,
        product_repository: IProductRepository,
    ) -> None:
        self._products = product_repository

    def execute(self, dto: DeactivateProductDTO) -> None:
        product = self._products.get_by_id(EntityId(dto.product_id))
        if product is None:
            raise ProductNotFoundException()

        product.deactivate()
