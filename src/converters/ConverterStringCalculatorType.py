from src.calculators.types.CalculatorType import CalculatorType


class ConverterStringCalculatorType:

    @staticmethod
    def to_calculator_type(key: str) -> CalculatorType:
        return CalculatorType[key]
