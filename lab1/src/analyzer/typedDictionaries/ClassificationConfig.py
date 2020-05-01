from typing import TypedDict

from src.classifiers.ClassifeirsTypes import ClassifierType
from src.classifiers.calculators.CalculatorType import CalculatorType


class NNClassification(TypedDict):
    type: ClassifierType  # accepts only NN
    calculator: CalculatorType


class KNNClassification(TypedDict):
    type: ClassifierType  # accepts only KNN
    calculator: CalculatorType
    k: int
