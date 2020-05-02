from src.classifiers.types.ClassifeirsTypes import ClassifierType


class ConverterStringClassifierType:

    @staticmethod
    def to_enum(key: str) -> ClassifierType:
        return ClassifierType[key]
