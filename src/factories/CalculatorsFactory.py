from src.calculators.AbstractCalculator import AbstractCalculator
from src.calculators.EuclidesDistanceCalculator import EuclidesDistanceCalculator
from src.calculators.StandardDevationCalculator import StandardDeviationCalculator
from src.calculators.types.CalculatorType import CalculatorType


class CalculatorsFactory:

    @staticmethod
    def get_calculator(calculator_type: CalculatorType) -> AbstractCalculator:
        if calculator_type == CalculatorType.DEVIATION:
            return StandardDeviationCalculator()
        if calculator_type == CalculatorType.EUCLIDES:
            return EuclidesDistanceCalculator()
