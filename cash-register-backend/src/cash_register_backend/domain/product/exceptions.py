from cash_register_backend.domain.shared import DomainException


class ProductIsInactiveException(DomainException):
    pass


class CannotChangePriceToZeroException(DomainException):
    pass


class ProductNotFoundException(DomainException):
    pass


class CannotAdjustStockForServiceException(DomainException):
    pass


class InsufficientStockException(DomainException):
    pass


class DuplicateSkuException(DomainException):
    pass
