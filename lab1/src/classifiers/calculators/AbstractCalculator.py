from abc import ABC, abstractmethod
from typing import List

import numpy as np


class AbstractCalculator(ABC):
    compared_traits: List[int]

    def __init__(self, compared_traits: List[int]) -> None:
        self.compared_traits = compared_traits

    @abstractmethod
    def calculate_similarity(self, compared_element: np.ndarray, reference_element: np.ndarray) -> float:
        pass
