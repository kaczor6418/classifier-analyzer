from typing import List

import numpy as np


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def get_only_x_points(points: List['Point']) -> List[float]:
        x_values: List[float] = []
        for point in points:
            x_values.append(point.x)
        return x_values

    @staticmethod
    def get_only_y_points(points: List['Point']) -> List[float]:
        y_values: List[float] = []
        for point in points:
            y_values.append(point.y)
        return y_values

    def calculate_distance_to_point(self, point: 'Point') -> float:
        return np.sqrt(((self.x - point.x) ** 2) + ((self.y - point.y) ** 2))
