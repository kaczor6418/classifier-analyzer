from typing import List

from src.calculators.types.CalculatorType import CalculatorType
from src.calculators.AbstractCalculator import AbstractCalculator
from src.calculators.EuclidesDistanceCalculator import EuclidesDistanceCalculator
from src.calculators.StandardDevationCalculator import StandardDeviationCalculator


class CalculatorsFactory:

    @staticmethod
    def get_calculator(calculator_type: CalculatorType, compared_traits: List[int]) -> AbstractCalculator:
        if calculator_type == CalculatorType.DEVIATION:
            return StandardDeviationCalculator(compared_traits)
        if calculator_type == CalculatorType.EUCLIDES:
            return EuclidesDistanceCalculator(compared_traits)
