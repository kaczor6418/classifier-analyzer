from typing import List

from src.ChartWizard import ChartWizard
from src.DataTable import DataTable
from src.Point import Point
from src.classifiers.ClassifierKNN import ClassifierKNN
from src.classifiers.ClassifierNN import ClassifierNN
from src.converters.ConverterDatasetElementsToPoints import ConverterDatasetElementsToPoints
from src.dictionaries.leafIdNameDictionary import leaf_id_and_name
from src.dictionaries.leafTraitIdNameDictionary import leaf_trait_id_and_name

csv_file_path = 'leaf/leaf.csv'
leaf_a_id = 3
leaf_b_id = 5
trait_x_id = 4
trait_y_id = 7


def run_nn_classification():
    leafs_database: DataTable = DataTable(csv_file_path, [leaf_a_id, leaf_b_id], [trait_x_id, trait_y_id])
    ChartWizard.set_chart_labels(leaf_trait_id_and_name.get(trait_x_id),
                                 leaf_trait_id_and_name.get(trait_y_id))
    for dataset in leafs_database.class_id_with_train_dataset.values():
        points: List[Point] = ConverterDatasetElementsToPoints.convert(dataset, leafs_database.chosen_traits[0],
                                                                       leafs_database.chosen_traits[1])
        ChartWizard.append_points(points, 'red', 's')
    for test_leaf in leafs_database.test_dataset:
        test_leaf_point: Point = test_leaf.create_point_from_traits(trait_x_id, trait_y_id)
        classifier_nn: ClassifierNN = ClassifierNN(leafs_database.train_dataset, [trait_x_id, trait_y_id])
        classified_leaf_id: int = classifier_nn.classify(test_leaf.metadata)
        ChartWizard.append_point_with_annotation_to_chart(test_leaf_point, leaf_id_and_name.get(classified_leaf_id),
                                                          'green', '*')
    ChartWizard.draw_chart()


def run_knn_classification():
    leafs_database: DataTable = DataTable(csv_file_path, [leaf_a_id, leaf_b_id], [trait_x_id, trait_y_id])
    ChartWizard.set_chart_labels(leaf_trait_id_and_name.get(trait_x_id),
                                 leaf_trait_id_and_name.get(trait_y_id))
    for dataset in leafs_database.class_id_with_train_dataset.values():
        points: List[Point] = ConverterDatasetElementsToPoints.convert(dataset, leafs_database.chosen_traits[0],
                                                                       leafs_database.chosen_traits[1])
        ChartWizard.append_points(points, 'blue', 'o')
    for test_leaf in leafs_database.test_dataset:
        test_leaf_point: Point = test_leaf.create_point_from_traits(trait_x_id, trait_y_id)
        classifier_knn: ClassifierKNN = ClassifierKNN(leafs_database.train_dataset, [trait_x_id, trait_y_id], 3)
        classified_leaf_id: int = classifier_knn.classify(test_leaf.metadata)
        ChartWizard.append_point_with_annotation_to_chart(test_leaf_point, leaf_id_and_name.get(classified_leaf_id),
                                                          'green', '*')
    ChartWizard.draw_chart()


run_nn_classification()
run_knn_classification()
