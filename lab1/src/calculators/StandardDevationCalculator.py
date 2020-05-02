from typing import List

import numpy as np

from src.calculators.AbstractCalculator import AbstractCalculator


class StandardDeviationCalculator(AbstractCalculator):
    def __init__(self, compared_traits: List[int]) -> None:
        super().__init__(compared_traits)

    def calculate_similarity(self, compared_element: np.ndarray, reference_element: np.ndarray) -> float:
        deviation: float = 0
        for trait_id in self.compared_traits:
            deviation += abs(reference_element[trait_id] - compared_element[trait_id])
        return deviation
