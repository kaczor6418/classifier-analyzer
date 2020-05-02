from typing import TypedDict, Optional

from src.calculators.types.CalculatorType import CalculatorType
from src.classifiers.types.ClassifeirsTypes import ClassifierType


class ClassificationSchema(TypedDict):
    type: ClassifierType
    calculator: CalculatorType
    k: Optional[int]
