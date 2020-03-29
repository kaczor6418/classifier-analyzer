import math
from typing import List

from src.Leaf import Leaf
from src.LeafsDatabase import LeafsDatabase
from src.Point import Point


class ClassifierNN:

    @staticmethod
    def classify(train_group: List[Leaf], test_element: Point, trait_x_id: int, trait_y_id: int) -> int:
        nearest_element_id_distance = ClassifierNN.create_nearest_element(-1, math.inf)
        for train_element in train_group:
            train_element_point: Point = train_element.make_point_from_traits(trait_x_id, trait_y_id)
            distance: float = test_element.calculate_distance_to_point(train_element_point)
            if distance < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifierNN.create_nearest_element(train_element.leaf_name_id, distance)
        return nearest_element_id_distance['leaf_name_id']

    @staticmethod
    def create_nearest_element(element_id: int, distance: float):
        return {
            'leaf_name_id': element_id,
            'distance': distance
        }
