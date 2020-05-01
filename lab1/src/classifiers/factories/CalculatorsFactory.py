from typing import List

from src.classifiers.calculators.CalculatorType import CalculatorType
from src.classifiers.calculators.AbstractCalculator import AbstractCalculator
from src.classifiers.calculators.EuclidesDistanceCalculator import EuclidesDistanceCalculator
from src.classifiers.calculators.StandardDevationCalculator import StandardDeviationCalculator


class CalculatorsFactory:
    standard_deviation_calculator: StandardDeviationCalculator
    euclides_distance_calculator: EuclidesDistanceCalculator

    def __init__(self, compared_traits: List[int]) -> None:
        self.standard_deviation_calculator = StandardDeviationCalculator(compared_traits)
        self.euclides_distance_calculator = EuclidesDistanceCalculator(compared_traits)

    def get_calculator(self, calculator_type: CalculatorType) -> AbstractCalculator:
        if calculator_type == CalculatorType.DEVIATION:
            return self.standard_deviation_calculator
        if calculator_type == CalculatorType.EUCLIDES:
            return self.euclides_distance_calculator
