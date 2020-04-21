from typing import List

import numpy as np

from src.classifiers.calculators.AbstractCalculator import AbstractCalculator
from src.utils.ClassifiersUtils import ClassifiersUtils


class EuclidesDistanceCalculator(AbstractCalculator):
    def __init__(self, compared_traits: List[int]) -> None:
        super().__init__(compared_traits)

    def calculate_similarity(self, compared_element: np.ndarray, reference_element: np.ndarray) -> float:
        compared_values: np.ndarray = np.array(
            ClassifiersUtils.get_values_by_indexes(compared_element, self.compared_traits))
        reference_values: np.ndarray = np.array(
            ClassifiersUtils.get_values_by_indexes(reference_element, self.compared_traits))
        return np.linalg.norm(compared_values - reference_values)
