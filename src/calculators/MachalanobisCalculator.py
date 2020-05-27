import numpy as np

from src.calculators.AbstractCalculator import AbstractCalculator


class MachalanobisCalculator(AbstractCalculator):
    def __init__(self) -> None:
        super().__init__()

    def calculate_similarity(self, compared_values: np.ndarray, reference_values: np.ndarray) -> float:
        compared_values_covriance_matrix = np.cov(compared_values.T)
        reference_values_covriance_matrix = np.cov(reference_values.T)
        return np.linalg.norm(compared_values - reference_values)
