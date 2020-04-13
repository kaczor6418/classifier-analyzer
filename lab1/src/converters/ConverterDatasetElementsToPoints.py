from typing import List

from src.DatasetElement import DatasetElement
from src.Point import Point


class ConverterDatasetElementsToPoints:

    @staticmethod
    def convert(dataset_elements: List[DatasetElement], trait_x: int, trait_y: int) -> List[Point]:
        points: List[Point] = []
        for leaf in dataset_elements:
            points.append(leaf.create_point_from_traits(trait_x, trait_y))
        return points
