from enum import Enum


class ProductType(str, Enum):
    UNIT = "unit"
    WEIGHT = "weight"
    SERVICE = "service"
