from typing import List

import numpy as np

from src.classifiers.typedDictionaries.NearestElement import NearestElement


class ClassifiersUtils:
    @staticmethod
    def create_nearest_element(element_id: int, distance: float) -> NearestElement:
        return {
            'element_id': element_id,
            'distance': distance
        }

    @staticmethod
    def get_values_by_indexes(array: np.ndarray, indexes: List[int]) -> List[float]:
        filtered_array: List[float] = []
        for i in indexes:
            filtered_array.append(array[i])
        return filtered_array
