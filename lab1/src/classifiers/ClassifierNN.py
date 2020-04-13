import math
from typing import List

from src.DatasetElement import DatasetElement
from src.Point import Point
from src.classifiers.typedDictionaries.NearestElement import NearestElement


class ClassifierNN:
    train_group: List[DatasetElement]

    def __init__(self, train_group: List[DatasetElement]) -> None:
        self.train_group = train_group

    def classify(self, test_element: Point, trait_x_id: int, trait_y_id: int) -> int:
        nearest_element_id_distance: NearestElement = ClassifierNN.create_nearest_element(-1, math.inf)
        for train_element in self.train_group:
            train_element_point: Point = train_element.create_point_from_traits(trait_x_id, trait_y_id)
            distance: float = test_element.calculate_distance_to_point(train_element_point)
            if distance < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifierNN.create_nearest_element(train_element.element_id, distance)
        return nearest_element_id_distance['element_id']

    @staticmethod
    def create_nearest_element(element_id: int, distance: float) -> NearestElement:
        return {
            'element_id': element_id,
            'distance': distance
        }
