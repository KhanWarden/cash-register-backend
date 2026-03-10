from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from cash_register_backend.domain.receipt import (
    IReceiptRepository,
    Receipt,
    ReceiptItem,
    Discount,
)
from cash_register_backend.domain.receipt.enums import ReceiptStatus
from cash_register_backend.domain.shared import EntityId, Money
from cash_register_backend.infrastructure.database.models import (
    ReceiptORM,
    ReceiptItemORM,
)


class ReceiptRepository(IReceiptRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def _item_to_entity(model: ReceiptItemORM) -> ReceiptItem:
        return ReceiptItem(
            id=EntityId(model.id),
            product_id=EntityId(model.product_id),
            product_name=model.product_name,
            product_price=Money(model.product_price),
            quantity=model.quantity,
        )

    @staticmethod
    def _to_entity(model: ReceiptORM) -> Receipt:
        return Receipt(
            id=EntityId(model.id),
            cashier_id=EntityId(model.cashier_id),
            status=ReceiptStatus(model.status),
            items=[ReceiptRepository._item_to_entity(i) for i in model.items],
            discount=Discount(model.discount) if model.discount else None,
            created_at=model.created_at,
            closed_at=model.closed_at,
        )

    @staticmethod
    def _to_model(receipt: Receipt) -> ReceiptORM:
        return ReceiptORM(
            id=receipt.id.value,
            cashier_id=receipt.cashier_id.value,
            status=receipt.status.value,
            discount=receipt.discount.value if receipt.discount else None,
            created_at=receipt.created_at,
            closed_at=receipt.closed_at,
            items=[
                ReceiptItemORM(
                    id=item.id.value,
                    receipt_id=receipt.id.value,
                    product_id=item.product_id.value,
                    product_name=item.product_name,
                    product_price=item.product_price.amount,
                    quantity=item.quantity,
                )
                for item in receipt.items
            ],
        )

    def get_by_id(self, receipt_id: EntityId) -> Receipt | None:
        result = self._session.execute(
            select(ReceiptORM)
            .where(ReceiptORM.id.is_(receipt_id.value))
            .options(joinedload(ReceiptORM.items))
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return self._to_entity(model)

    def get_by_cashier(self, cashier_id: EntityId) -> list[Receipt] | None:
        result = self._session.execute(
            select(ReceiptORM)
            .where(ReceiptORM.cashier_id.is_(cashier_id.value))
            .options(joinedload(ReceiptORM.items))
        )
        return [self._to_entity(row) for row in result.unique().scalars().all()]

    def save(self, receipt: Receipt) -> None:
        model = self._session.get(
            ReceiptORM,
            receipt.id.value,
            options=[joinedload(ReceiptORM.items)],
        )
        if model is None:
            self._session.add(self._to_model(receipt))
        else:
            model.status = receipt.status.value
            model.discount = receipt.discount.value if receipt.discount else None
            model.closed_at = receipt.closed_at
        self._session.flush()
