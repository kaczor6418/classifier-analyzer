import numpy as np

from src.calculators.AbstractCalculator import AbstractCalculator


class StandardDeviationCalculator(AbstractCalculator):
    def __init__(self, ) -> None:
        super().__init__()

    def calculate_similarity(self, compared_element: np.ndarray, reference_element: np.ndarray) -> float:
        deviation: float = 0
        for i in range(len(compared_element)):
            deviation += abs(reference_element[i] - compared_element[i])
        return deviation
