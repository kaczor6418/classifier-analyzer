from src.calculators.types.CalculatorType import CalculatorType


class ConverterStringCalculatorType:

    @staticmethod
    def to_enum(key: str) -> CalculatorType:
        return CalculatorType[key]
