import math
from typing import List

import numpy as np

from src.structures.DatasetElement import DatasetElement
from src.classifiers.calculatorFactory.CalculatorType import CalculatorType
from src.classifiers.calculatorFactory.CalculatorsFactory import CalculatorsFactory
from src.classifiers.calculators.AbstractCalculator import AbstractCalculator
from src.classifiers.typedDictionaries.NearestElement import NearestElement
from src.utils.ClassifiersUtils import ClassifiersUtils


class ClassifierNN:
    train_group: List[DatasetElement]
    calculator: AbstractCalculator

    def __init__(self, train_group: List[DatasetElement], compared_traits: List[int],
                 calculator_type: CalculatorType = CalculatorType.EUCLIDES) -> None:
        calculator_factory: CalculatorsFactory = CalculatorsFactory(compared_traits)
        self.train_group = train_group
        self.calculator = calculator_factory.get_calculator(calculator_type)

    def classify(self, test_element: np.ndarray) -> int:
        nearest_element_id_distance: NearestElement = ClassifiersUtils.create_nearest_element(-1, math.inf)
        for train_element in self.train_group:
            distance: float = self.calculator.calculate_similarity(test_element, train_element.metadata)
            if distance < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifiersUtils.create_nearest_element(train_element.element_id,
                                                                                      distance)
        return nearest_element_id_distance['element_id']
