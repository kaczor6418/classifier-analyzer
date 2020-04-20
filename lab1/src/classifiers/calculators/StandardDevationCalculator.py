from typing import List

from src.DatasetElement import DatasetElement


class StandardDeviationCalculator:
    compared_traits: List[int]

    def __init__(self, compared_traits: List[int]) -> None:
        self.compared_traits = compared_traits

    def calculate_similarity(self, compared_element: DatasetElement, reference_element: DatasetElement) -> float:
        deviation: float = 0
        for trait_id in self.compared_traits:
            deviation += abs(reference_element.metadata[trait_id] - compared_element.metadata[trait_id])
        return deviation
