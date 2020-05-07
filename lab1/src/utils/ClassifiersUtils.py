from typing import List

import numpy as np

from src.classifiers.types.NearestElement import NearestElement


class ClassifiersUtils:
    @staticmethod
    def create_nearest_element(element_id: int, distance: float) -> NearestElement:
        return {
            'element_class_id': element_id,
            'distance': distance
        }

    @staticmethod
    def get_values_by_indexes(array: np.ndarray, indexes: List[int]) -> np.ndarray:
        return np.array([array[i] for i in indexes])
