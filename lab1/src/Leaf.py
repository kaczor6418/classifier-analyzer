import numpy as np
from src.Point import Point


class Leaf:
    metadata: np.ndarray
    leaf_name_id: int

    def __init__(self, metadata: np.ndarray):
        self.metadata = metadata
        self.leaf_name_id = self.metadata[0]

    def create_point_from_traits(self, trait_x_id: int, trait_y_id: int) -> Point:
        return Point(self.metadata[trait_x_id], self.metadata[trait_y_id])
