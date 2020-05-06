from src.classifiers.types.ClassifeirsTypes import ClassifierType


class ConverterStringClassifierType:

    @staticmethod
    def to_classifier_type(key: str) -> ClassifierType:
        return ClassifierType[key]
