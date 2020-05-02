from typing import TypedDict

from src.classifiers.types.ClassifeirsTypes import ClassifierType
from src.calculators.types.CalculatorType import CalculatorType


class NNClassification(TypedDict):
    type: ClassifierType  # accepts only NN
    calculator: CalculatorType


class KNNClassification(TypedDict):
    type: ClassifierType  # accepts only KNN
    calculator: CalculatorType
    k: int
