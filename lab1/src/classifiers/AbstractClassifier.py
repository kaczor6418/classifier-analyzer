from abc import ABC, abstractmethod
from typing import List

import numpy as np

from src.calculators.AbstractCalculator import AbstractCalculator
from src.calculators.types.CalculatorType import CalculatorType
from src.factories.CalculatorsFactory import CalculatorsFactory
from src.structures.DatasetElement import DatasetElement


class AbstractClassifier(ABC):
    train_group: List[DatasetElement]
    calculator: AbstractCalculator

    def __init__(self, train_group: List[DatasetElement], compared_traits: List[int],
                 calculator_type: CalculatorType) -> None:
        self.train_group = train_group
        self.calculator = CalculatorsFactory.get_calculator(calculator_type, compared_traits)

    @abstractmethod
    def classify(self, test_element: np.ndarray) -> int:
        pass
