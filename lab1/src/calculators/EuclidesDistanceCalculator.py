import numpy as np

from src.calculators.AbstractCalculator import AbstractCalculator


class EuclidesDistanceCalculator(AbstractCalculator):
    def __init__(self) -> None:
        super().__init__()

    def calculate_similarity(self, compared_values: np.ndarray, reference_values: np.ndarray) -> float:
        return np.linalg.norm(compared_values - reference_values)
