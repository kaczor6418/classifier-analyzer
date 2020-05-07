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
        self.set_average_positions(compared_traits, classes_ids)

    @staticmethod
    def get_traits_values_from_dataset(dataset: DatasetElement, compared_traits: List[int]) -> np.ndarray:
        trait_values: List[float] = []
        for trait in compared_traits:
            trait_values.append(dataset.metadata[trait])
        return np.array(trait_values)

    def set_average_positions(self, compared_traits: List[int], classes_ids: List[int]):
        for dataset in self.train_group:
            if dataset.element_class_id in classes_ids:
                trait_values: np.ndarray = self.get_traits_values_from_dataset(dataset, compared_traits)
                if dataset.element_class_id in self.average_classes_positions:
                    current_values: np.ndarray = self.average_classes_positions[dataset.element_class_id]
                    self.average_classes_positions[dataset.element_class_id] = np.add(current_values, trait_values)
                else:
                    self.average_classes_positions[dataset.element_class_id] = trait_values

    def classify(self, test_element: np.ndarray) -> int:
        nearest_element_id_distance: NearestElement = ClassifiersUtils.create_nearest_element(-1, math.inf)
        for class_id, class_average_position in self.average_classes_positions.items():
            distance: float = self.calculator.calculate_similarity(test_element, class_average_position)
            if distance < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifiersUtils.create_nearest_element(class_id, distance)
        return nearest_element_id_distance['element_class_id']
