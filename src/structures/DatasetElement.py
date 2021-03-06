import numpy as np
from src.structures.Point import Point


class DatasetElement:
    metadata: np.ndarray
    element_class_id: int

    def __init__(self, metadata: np.ndarray) -> None:
        self.metadata = metadata
        self.element_class_id = self.metadata[0]

    def create_point_from_traits(self, trait_x_id: int, trait_y_id: int) -> Point:
        return Point(self.metadata[trait_x_id], self.metadata[trait_y_id])
