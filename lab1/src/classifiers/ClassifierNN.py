import math
from typing import List

import numpy as np

from src.calculators.types.CalculatorType import CalculatorType
from src.classifiers.AbstractClassifier import AbstractClassifier
from src.classifiers.types.NearestElement import NearestElement
from src.structures.DatasetElement import DatasetElement
from src.utils.ClassifiersUtils import ClassifiersUtils


class ClassifierNN(AbstractClassifier):

    def __init__(self, train_group: List[DatasetElement], compared_traits: List[int],
                 calculator_type: CalculatorType) -> None:
        super().__init__(train_group, compared_traits, calculator_type)

    def classify(self, test_element: np.ndarray) -> int:
        nearest_element_id_distance: NearestElement = ClassifiersUtils.create_nearest_element(-1, math.inf)
        test_traits_values: np.ndarray = ClassifiersUtils.get_values_by_indexes(test_element,
                                                                                self.compared_traits)
        for train_element in self.train_group:
            train_traits_values: np.ndarray = ClassifiersUtils.get_values_by_indexes(train_element.metadata,
                                                                                     self.compared_traits)
            distance: float = self.calculator.calculate_similarity(test_traits_values, train_traits_values)
            if distance < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifiersUtils.create_nearest_element(train_element.element_class_id,
                                                                                      distance)
        return nearest_element_id_distance['element_class_id']
