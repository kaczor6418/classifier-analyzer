import time
from typing import List

from src.analyzer.types.AnalyzerSchema import AnalyzerSchema
from src.analyzer.types.ClassesSchema import ClassSchema
from src.analyzer.types.ClassificationSchema import ClassificationSchema
from src.analyzer.types.ClassifiedElementSchema import ClassifiedElementSchema
from src.classifiers.AbstractClassifier import AbstractClassifier
from src.converters.ConverterDatasetElementsPoints import ConverterDatasetElementsPoints
from src.dictionaries.leafIdNameDictionary import leaf_id_and_name
from src.dictionaries.leafTraitIdNameDictionary import leaf_trait_id_and_name
from src.drawers.ChartWizard import ChartWizard
from src.factories.ClassifiersFactory import ClassifiersFactory
from src.structures.DataTable import DataTable
from src.structures.Point import Point
from src.utils.Utils import Utils


class Analyzer:
    classification_time: float = 0.0
    invalid_classifications_counter: int = 0
    valid_classifications_counter: int = 0

    x_axis_trait_id: int
    y_axis_trait_id: int
    datatable: DataTable
    classifier: AbstractClassifier
    classes_config: List[ClassSchema]
    classified_element_config: ClassifiedElementSchema = dict()

    def __init__(self, config: AnalyzerSchema) -> None:
        self.datatable = self.create_datatable(config['csv_file_path'], config['traits_ids'], config['classes_config'],
                                               config['test_group_size'])
        self.classifier = ClassifiersFactory.get_classifier(config['classification_config'],
                                                            self.datatable.train_dataset,
                                                            self.datatable.chosen_traits,
                                                            list(self.datatable.class_id_with_train_dataset.keys()))
        self.x_axis_trait_id = config['x_axis_trait_id']
        self.y_axis_trait_id = config['y_axis_trait_id']
        self.classes_config = config['classes_config']
        self.classified_element_config = config['classified_element_config']
        self.init_chart_wizard(config['classification_config'])

    @staticmethod
    def create_datatable(csv_file_path: str, traits_ids: List[int], classes_config: List[ClassSchema],
                         test_group_size: float) -> DataTable:
        classes_ids = list(map(lambda class_item: class_item['id'], classes_config))
        return DataTable(csv_file_path, classes_ids, traits_ids, test_group_size)

    @staticmethod
    def build_chart_title(classifier: ClassificationSchema) -> str:
        return 'Classification: ' + classifier['type'].value + ', Calculator: ' + classifier['calculator'].value

    def update_classifier_effectiveness(self, classified_id: int, original_id: int) -> None:
        if classified_id == original_id:
            self.valid_classifications_counter += 1
        else:
            self.invalid_classifications_counter += 1

    def init_chart_wizard(self, classifier: ClassificationSchema) -> None:
        ChartWizard.set_chart_title(Analyzer.build_chart_title(classifier))
        ChartWizard.set_chart_labels(leaf_trait_id_and_name.get(self.x_axis_trait_id),
                                     leaf_trait_id_and_name.get(self.y_axis_trait_id))

    def run_analysis(self) -> None:
        for class_id, dataset in self.datatable.class_id_with_train_dataset.items():
            points: List[Point] = ConverterDatasetElementsPoints.to_points(dataset, self.x_axis_trait_id,
                                                                           self.y_axis_trait_id)
            point_color: str = Utils.get_key_value_by_id_from_dictionaries(self.classes_config, class_id, 'point_color')
            point_marker: str = Utils.get_key_value_by_id_from_dictionaries(self.classes_config, class_id,
                                                                            'point_marker')
            ChartWizard.append_points(points, point_color, point_marker, leaf_id_and_name.get(class_id))
        for test_item in self.datatable.test_dataset:
            test_point: Point = test_item.create_point_from_traits(self.x_axis_trait_id, self.y_axis_trait_id)
            start: float = time.process_time()
            classified_element_id: int = self.classifier.classify(test_item.metadata)
            end: float = time.process_time()
            self.classification_time += (end - start)
            self.update_classifier_effectiveness(classified_element_id, test_item.element_class_id)
            ChartWizard.append_point_with_annotation_to_chart(test_point, leaf_id_and_name.get(classified_element_id),
                                                              self.classified_element_config['point_color'],
                                                              self.classified_element_config['point_marker'])

    def calculate_classification_effectiveness(self) -> float:
        return self.valid_classifications_counter / (
                self.valid_classifications_counter + self.invalid_classifications_counter)

    def show_results(self) -> None:
        print('Time needed for classification: ' + str(self.classification_time))
        print('Valid classifications count: ' + str(self.valid_classifications_counter))
        print('Invalid classifications count: ' + str(self.invalid_classifications_counter))
        print('Classification effectiveness: ' + '{:.2%}'.format(self.calculate_classification_effectiveness()))
        ChartWizard.draw_chart()
        print('-------------------------------------------------------------------------------------------------------')
