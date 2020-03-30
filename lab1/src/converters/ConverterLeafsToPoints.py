from typing import List

from src.Leaf import Leaf
from src.Point import Point


class ConverterLeafsToPoints:

    @staticmethod
    def convert(leafs: List[Leaf], trait_x: int, trait_y: int) -> List[Point]:
        points: List[Point] = []
        for leaf in leafs:
            points.append(leaf.create_point_from_traits(trait_x, trait_y))
        return points
