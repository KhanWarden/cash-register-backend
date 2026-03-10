from sqlalchemy import select
from sqlalchemy.orm import Session

from cash_register_backend.domain.payment import IPaymentRepository, Payment
from cash_register_backend.domain.receipt.enums import PaymentMethod
from cash_register_backend.domain.shared import EntityId, Money
from cash_register_backend.infrastructure.database.models.payment import PaymentORM


class PaymentRepository(IPaymentRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def _to_entity(model: PaymentORM) -> Payment:
        return Payment(
            id=EntityId(model.id),
            receipt_id=EntityId(model.receipt_id),
            cashier_id=EntityId(model.cashier_id),
            method=PaymentMethod(model.method),
            amount=Money(model.amount),
            created_at=model.created_at,
        )

    @staticmethod
    def _to_model(payment: Payment) -> PaymentORM:
        return PaymentORM(
            id=payment.id.value,
            receipt_id=payment.receipt_id.value,
            cashier_id=payment.cashier_id.value,
            method=payment.method.value,
            amount=payment.method.value,
            created_at=payment.created_at,
        )

    def get_by_payment_id(self, payment_id: EntityId) -> Payment | None:
        model: PaymentORM | None = self._session.get(PaymentORM, payment_id.value)
        if model is None:
            return None
        return self._to_entity(model)

    def get_by_receipt_id(self, receipt_id: EntityId) -> list[Payment]:
        result = self._session.execute(
            select(PaymentORM).where(PaymentORM.receipt_id.is_(receipt_id))
        )
        return [self._to_entity(row) for row in result.scalars().all()]

    def get_by_cashier_id(self, cashier_id: EntityId) -> list[Payment] | None:
        result = self._session.execute(
            select(PaymentORM).where(PaymentORM.cashier_id.is_(cashier_id))
        )
        return [self._to_entity(row) for row in result.scalars().all()]

    def save(self, payment: Payment) -> None:
        model = self._session.get(PaymentORM, payment.id.value)
        if model is None:
            self._session.add(self._to_model(payment))
        else:
            model.method = payment.method.value
            model.amount = payment.amount.amount
        self._session.flush()
