from enum import Enum


class MeasurementUnit(str, Enum):
    PIECE = "piece"  # штука
    KG = "kg"  # килограмм
    GRAM = "gram"  # грамм
    LITER = "liter"  # литр
    SERVICE = "service"  # услуга
