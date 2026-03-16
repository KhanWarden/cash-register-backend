__all__ = (
    # User
    "CreateUserDTO",
    "LoginDTO",
    "ChangeRoleDTO",
    "ActivateUserDTO",
    "DeactivateUserDTO",
    # Category
    "CreateCategoryDTO",
    "UpdateCategoryDTO",
    "DeactivateCategoryDTO",
    # Product
    "CreateProductDTO",
    "UpdateProductDTO",
    "AddStockDTO",
    "DeactivateProductDTO",
)

from .user import (
    CreateUserDTO,
    LoginDTO,
    ChangeRoleDTO,
    ActivateUserDTO,
    DeactivateUserDTO,
)
from .category import CreateCategoryDTO, UpdateCategoryDTO, DeactivateCategoryDTO
from .product import (
    CreateProductDTO,
    UpdateProductDTO,
    AddStockDTO,
    DeactivateProductDTO,
)
