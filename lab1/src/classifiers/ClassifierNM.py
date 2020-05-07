import math
from typing import List, Dict

import numpy as np

from src.calculators.types.CalculatorType import CalculatorType
from src.classifiers.AbstractClassifier import AbstractClassifier
from src.classifiers.types.NearestElement import NearestElement
from src.structures.DatasetElement import DatasetElement
from src.utils.ClassifiersUtils import ClassifiersUtils


class ClassifierNM(AbstractClassifier):
    average_classes_positions: Dict[int, np.ndarray] = dict()

    def __init__(self, train_group: List[DatasetElement], compared_traits: List[int],
                 calculator_type: CalculatorType, classes_ids: List[int]) -> None:
        super().__init__(train_group, compared_traits, calculator_type)
        self.set_average_positions(classes_ids)

    def set_average_positions(self, classes_ids: List[int]):
        class_number_of_occurrences: Dict[int, int] = dict()
        for dataset in self.train_group:
            if dataset.element_class_id in classes_ids:
                trait_values: np.ndarray = ClassifiersUtils.get_values_by_indexes(dataset.metadata,
                                                                                  self.compared_traits)
                if dataset.element_class_id in self.average_classes_positions:
                    current_values: np.ndarray = self.average_classes_positions[dataset.element_class_id]
                    self.average_classes_positions[dataset.element_class_id] = np.add(current_values, trait_values)
                    class_number_of_occurrences[dataset.element_class_id] += 1
                else:
                    self.average_classes_positions[dataset.element_class_id] = trait_values
                    class_number_of_occurrences[dataset.element_class_id] = 1
        for class_id, class_average_positions in self.average_classes_positions.items():
            number_of_occurrences = class_number_of_occurrences[class_id]
            for i in range(len(class_average_positions)):
                class_average_positions[i] = class_average_positions[i] / number_of_occurrences

    def classify(self, test_element: np.ndarray) -> int:
        nearest_element_id_distance: NearestElement = ClassifiersUtils.create_nearest_element(-1, math.inf)
        test_traits_values: np.ndarray = ClassifiersUtils.get_values_by_indexes(test_element,
                                                                                self.compared_traits)
        for class_id, class_average_position in self.average_classes_positions.items():
            distance: float = self.calculator.calculate_similarity(test_traits_values, class_average_position)
            if distance < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifiersUtils.create_nearest_element(class_id, distance)
        return nearest_element_id_distance['element_class_id']
