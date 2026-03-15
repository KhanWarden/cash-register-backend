from cash_register_backend.domain.shared import DomainException


class DuplicateCategoryNameException(DomainException):
    pass


class CategoryNotFoundException(DomainException):
    pass
