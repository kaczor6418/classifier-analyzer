from typing import List

from src.analyzer.types.ClassificationSchema import ClassificationSchema
from src.classifiers.AbstractClassifier import AbstractClassifier
from src.classifiers.ClassifierKNN import ClassifierKNN
from src.classifiers.ClassifierNN import ClassifierNN
from src.classifiers.types.ClassifeirsTypes import ClassifierType
from src.structures.DatasetElement import DatasetElement


class ClassifiersFactory:

    @staticmethod
    def get_classifier(classifier_config: ClassificationSchema, train_group: List[DatasetElement],
                       compared_traits: List[int]) -> AbstractClassifier:
        if classifier_config['type'] == ClassifierType.NN:
            return ClassifierNN(train_group, compared_traits, classifier_config['calculator'])
        if classifier_config['type'] == ClassifierType.KNN:
            return ClassifierKNN(train_group, compared_traits, classifier_config['calculator'], classifier_config['k'])
