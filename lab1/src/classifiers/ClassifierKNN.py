import math
from typing import List, Dict

import numpy as np

from src.structures.DatasetElement import DatasetElement
from src.classifiers.calculators.CalculatorType import CalculatorType
from src.classifiers.factories.CalculatorsFactory import CalculatorsFactory
from src.classifiers.calculators.AbstractCalculator import AbstractCalculator
from src.classifiers.typedDictionaries.NearestElement import NearestElement
from src.utils.ClassifiersUtils import ClassifiersUtils


class ClassifierKNN:
    train_group: List[DatasetElement]
    calculator: AbstractCalculator
    k: int

    def __init__(self, train_group: List[DatasetElement], compared_traits: List[int], k: int,
                 calculator_type: CalculatorType = CalculatorType.EUCLIDES) -> None:
        calculator_factory: CalculatorsFactory = CalculatorsFactory(compared_traits)
        self.k = k
        self.train_group = train_group
        self.calculator = calculator_factory.get_calculator(calculator_type)

    def classify(self, test_element: np.ndarray) -> int:
        nearest_element_id_distance: NearestElement = ClassifiersUtils.create_nearest_element(-1, math.inf)
        elements_id_distances: Dict[int, List[float]] = dict()
        for train_element in self.train_group:
            distance: float = self.calculator.calculate_similarity(test_element, train_element.metadata)
            if elements_id_distances.get(train_element.element_id) is None:
                elements_id_distances[train_element.element_id] = [distance]
            else:
                elements_id_distances.get(train_element.element_id).append(distance)
        for nn_id, nn_distances in elements_id_distances.items():
            sum_of_distances_to_k_nn = sum(sorted(nn_distances, key=float)[:self.k])
            if sum_of_distances_to_k_nn < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifiersUtils.create_nearest_element(nn_id, sum_of_distances_to_k_nn)
        return nearest_element_id_distance['element_id']
