from abc import ABC, abstractmethod

import numpy as np


class AbstractCalculator(ABC):

    @abstractmethod
    def calculate_similarity(self, compared_element: np.ndarray, reference_element: np.ndarray) -> float:
        pass
