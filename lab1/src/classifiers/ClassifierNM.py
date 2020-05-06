from typing import List, Dict

import numpy as np

from src.calculators.types.CalculatorType import CalculatorType
from src.classifiers.AbstractClassifier import AbstractClassifier
from src.structures.DatasetElement import DatasetElement


class ClassifierNM(AbstractClassifier):
    average_positions: Dict[int, List[float]] = dict()

    def __init__(self, train_group: List[DatasetElement], compared_traits: List[int],
                 calculator_type: CalculatorType, classes_ids: List[int]) -> None:
        super().__init__(train_group, compared_traits, calculator_type)
        self.set_average_positions(compared_traits, classes_ids)

    @staticmethod
    def get_traits_values_from_dataset(dataset: DatasetElement, compared_traits: List[int]) -> List[float]:
        trait_values: List[float] = []
        for trait in compared_traits:
            trait_values.append(dataset.metadata[trait])
        return trait_values

    def set_average_positions(self, compared_traits: List[int], classes_ids: List[int]):
        for dataset in self.train_group:
            if dataset.element_class_id in classes_ids:
                trait_values: List[float] = self.get_traits_values_from_dataset(dataset, compared_traits)
                if dataset.element_class_id in self.average_positions:
                    self.average_positions[dataset.element_class_id] = trait_values
                else:
                    current_values: List[float] = self.average_positions[dataset.element_class_id]
                    self.average_positions[dataset.element_class_id] = np.add(current_values, trait_values)

    def classify(self, test_element: np.ndarray) -> int:
        pass
