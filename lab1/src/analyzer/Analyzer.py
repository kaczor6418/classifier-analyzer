from typing import List, Union

from src.analyzer.types.AnalyzerSchema import AnalyzerSchema
from src.analyzer.types.ClassesSchema import ClassSchema
from src.analyzer.types.ClassificationSchema import NNClassification, KNNClassification
from src.analyzer.types.ClassifiedElementSchema import ClassifiedElementSchema
from src.converters.ConverterDatasetElementsToPoints import ConverterDatasetElementsToPoints
from src.dictionaries.leafTraitIdNameDictionary import leaf_trait_id_and_name
from src.drawers.ChartWizard import ChartWizard
from src.structures.DataTable import DataTable
from src.structures.Point import Point
from src.utils.Utils import Utils


class Analyzer:
    x_axis_trait_id: int
    y_axis_trait_id: int
    datatable: DataTable
    classes_config: List[ClassSchema]
    classification_config: Union[NNClassification, KNNClassification]
    classified_element_config: ClassifiedElementSchema

    def __init__(self, config: AnalyzerSchema) -> None:
        self.datatable = self.create_datatable(config['csv_file_path'], config['traits_ids'], config['classes_config'],
                                               config['test_group_size'])
        self.x_axis_trait_id = config['x_axis_trait_id']
        self.y_axis_trait_id = config['y_axis_trait_id']
        self.classes_config = config['classes_config']
        self.classification_config = config['classification_config']
        if 'classified_element' in config:
            self.classified_element_config = config['classified_element_config']
        else:
            self.classified_element_config['point_color'] = 'green'
            self.classified_element_config['point_marker'] = '*'

    def create_datatable(self, csv_file_path: str, traits_ids: List[int], classes_config: List[ClassSchema],
                         test_group_size: int) -> DataTable:
        classes_ids = list(map(lambda class_item: class_item['id'], classes_config))
        return DataTable(csv_file_path, classes_ids, traits_ids, test_group_size)

    def run_analysis(self) -> None:
        ChartWizard.set_chart_labels(leaf_trait_id_and_name.get(self.x_axis_trait_id),
                                     leaf_trait_id_and_name.get(self.y_axis_trait_id))
        for key, dataset in self.datatable.class_id_with_train_dataset.items():
            points: List[Point] = ConverterDatasetElementsToPoints.convert(dataset, self.x_axis_trait_id,
                                                                           self.y_axis_trait_id)
            point_color: str = Utils.get_key_value_by_id_from_dictionaries(self.classes_config, key, 'point_color')
            point_marker: str = Utils.get_key_value_by_id_from_dictionaries(self.classes_config, key, 'point_marker')
            ChartWizard.append_points(points, point_color, point_marker)
        for test_item in self.datatable.test_dataset:
            test_leaf_point: Point = test_item.create_point_from_traits(self.x_axis_trait_id, self.y_axis_trait_id)
