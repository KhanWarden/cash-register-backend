from cash_register_backend.domain.shared import DomainException


class ReceiptCannotBeRefundedException(DomainException):
    pass


class ProductIsInactiveForSaleException(DomainException):
    pass


class InsufficientStockForReceiptException(DomainException):
    pass


class EmptyReceiptCannotBeCreatedException(DomainException):
    pass
