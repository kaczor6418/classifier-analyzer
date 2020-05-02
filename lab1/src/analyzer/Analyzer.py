from typing import List

from src.analyzer.types.AnalyzerSchema import AnalyzerSchema
from src.analyzer.types.ClassesSchema import ClassSchema
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
                                                            self.datatable.chosen_traits)
        self.x_axis_trait_id = config['x_axis_trait_id']
        self.y_axis_trait_id = config['y_axis_trait_id']
        self.classes_config = config['classes_config']
        self.classified_element_config = config['classified_element_config']

    def create_datatable(self, csv_file_path: str, traits_ids: List[int], classes_config: List[ClassSchema],
                         test_group_size: float) -> DataTable:
        classes_ids = list(map(lambda class_item: class_item['id'], classes_config))
        return DataTable(csv_file_path, classes_ids, traits_ids, test_group_size)

    def run_analysis(self) -> None:
        ChartWizard.set_chart_labels(leaf_trait_id_and_name.get(self.x_axis_trait_id),
                                     leaf_trait_id_and_name.get(self.y_axis_trait_id))
        for key, dataset in self.datatable.class_id_with_train_dataset.items():
            points: List[Point] = ConverterDatasetElementsPoints.to_points(dataset, self.x_axis_trait_id,
                                                                           self.y_axis_trait_id)
            point_color: str = Utils.get_key_value_by_id_from_dictionaries(self.classes_config, key, 'point_color')
            point_marker: str = Utils.get_key_value_by_id_from_dictionaries(self.classes_config, key, 'point_marker')
            ChartWizard.append_points(points, point_color, point_marker)
        for test_item in self.datatable.test_dataset:
            test_point: Point = test_item.create_point_from_traits(self.x_axis_trait_id, self.y_axis_trait_id)
            classified_element_id: int = self.classifier.classify(test_item.metadata)
            ChartWizard.append_point_with_annotation_to_chart(test_point, leaf_id_and_name.get(classified_element_id),
                                                              self.classified_element_config['point_color'],
                                                              self.classified_element_config['point_marker'])
        ChartWizard.draw_chart()
