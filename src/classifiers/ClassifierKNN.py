import math
from typing import List, Dict

import numpy as np

from src.calculators.types.CalculatorType import CalculatorType
from src.classifiers.AbstractClassifier import AbstractClassifier
from src.classifiers.types.NearestElement import NearestElement
from src.structures.DatasetElement import DatasetElement
from src.utils.ClassifiersUtils import ClassifiersUtils


class ClassifierKNN(AbstractClassifier):
    k: int = 3

    def __init__(self, train_group: List[DatasetElement], compared_traits: List[int], calculator_type: CalculatorType,
                 k: int) -> None:
        super().__init__(train_group, compared_traits, calculator_type)
        self.k = k

    def classify(self, test_element: np.ndarray) -> int:
        nearest_element_id_distance: NearestElement = ClassifiersUtils.create_nearest_element(-1, math.inf)
        elements_class_id_distances: Dict[int, List[float]] = dict()
        test_traits_values: np.ndarray = ClassifiersUtils.get_values_by_indexes(test_element,
                                                                                self.compared_traits)
        for train_element in self.train_group:
            train_traits_values: np.ndarray = ClassifiersUtils.get_values_by_indexes(train_element.metadata,
                                                                                     self.compared_traits)
            distance: float = self.calculator.calculate_similarity(test_traits_values, train_traits_values)
            if elements_class_id_distances.get(train_element.element_class_id) is None:
                elements_class_id_distances[train_element.element_class_id] = [distance]
            else:
                elements_class_id_distances.get(train_element.element_class_id).append(distance)
        for nn_id, nn_distances in elements_class_id_distances.items():
            sum_of_distances_to_k_nn = sum(sorted(nn_distances, key=float)[:self.k])
            if sum_of_distances_to_k_nn < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifiersUtils.create_nearest_element(nn_id, sum_of_distances_to_k_nn)
        return nearest_element_id_distance['element_class_id']
