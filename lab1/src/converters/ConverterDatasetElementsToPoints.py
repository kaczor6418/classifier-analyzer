from typing import List

from src.structures.DatasetElement import DatasetElement
from src.structures.Point import Point


class ConverterDatasetElementsToPoints:

    @staticmethod
    def convert(dataset_elements: List[DatasetElement], trait_x: int, trait_y: int) -> List[Point]:
        points: List[Point] = []
        for dataset_element in dataset_elements:
            points.append(dataset_element.create_point_from_traits(trait_x, trait_y))
        return points
