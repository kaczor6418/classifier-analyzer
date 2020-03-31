from src.ChartWizard import ChartWizard
from src.LeafsDatabase import LeafsDatabase
from src.Point import Point
from src.classifiers.ClassifierKNN import ClassifierKNN
from src.classifiers.ClassifierNN import ClassifierNN
from src.converters.ConverterLeafsToPoints import ConverterLeafsToPoints
from src.dictionaries.leafIdNameDictionary import leaf_id_and_name
from src.dictionaries.leafTraitIdNameDictionary import leaf_trait_id_and_name

csv_file_path = 'leaf/leaf.csv'
leaf_a_id = 3
leaf_b_id = 5
trait_x_id = 4
trait_y_id = 7


def run_nn_classification():
    leafs_database: LeafsDatabase = LeafsDatabase(csv_file_path, leaf_a_id, leaf_b_id, trait_x_id, trait_y_id)
    chart_drawer: ChartWizard = ChartWizard(leaf_trait_id_and_name.get(trait_x_id),
                                            leaf_trait_id_and_name.get(trait_y_id))
    for test_leaf in leafs_database.test_leafs:
        test_leaf_point: Point = test_leaf.create_point_from_traits(trait_x_id, trait_y_id)
        classified_leaf_id: int = ClassifierNN.classify(leafs_database.train_leafs, test_leaf_point,
                                                        leafs_database.trait_x_id, leafs_database.trait_y_id)
        if classified_leaf_id == leaf_a_id:
            chart_drawer.append_element_with_annotation_to_chart(test_leaf_point, leaf_id_and_name.get(leaf_a_id))
        else:
            chart_drawer.append_element_with_annotation_to_chart(test_leaf_point, leaf_id_and_name.get(leaf_b_id))
    chart_drawer.draw_2d_chart(
        ConverterLeafsToPoints.convert(leafs_database.train_leafs_a, leafs_database.trait_x_id,
                                       leafs_database.trait_y_id),
        ConverterLeafsToPoints.convert(leafs_database.train_leafs_b, leafs_database.trait_x_id,
                                       leafs_database.trait_y_id))


def run_knn_classification():
    leafs_database: LeafsDatabase = LeafsDatabase(csv_file_path, leaf_a_id, leaf_b_id, trait_x_id, trait_y_id)
    chart_drawer: ChartWizard = ChartWizard(leaf_trait_id_and_name.get(trait_x_id),
                                            leaf_trait_id_and_name.get(trait_y_id))
    for test_leaf in leafs_database.test_leafs:
        test_leaf_point: Point = test_leaf.create_point_from_traits(trait_x_id, trait_y_id)
        classified_leaf_id: int = ClassifierKNN.classify(leafs_database.train_leafs, test_leaf_point,
                                                         leafs_database.trait_x_id, leafs_database.trait_y_id, 3)
        if classified_leaf_id == leaf_a_id:
            chart_drawer.append_element_with_annotation_to_chart(test_leaf_point, leaf_id_and_name.get(leaf_a_id))
        else:
            chart_drawer.append_element_with_annotation_to_chart(test_leaf_point, leaf_id_and_name.get(leaf_b_id))
    chart_drawer.draw_2d_chart(
        ConverterLeafsToPoints.convert(leafs_database.train_leafs_a, leafs_database.trait_x_id,
                                       leafs_database.trait_y_id),
        ConverterLeafsToPoints.convert(leafs_database.train_leafs_b, leafs_database.trait_x_id,
                                       leafs_database.trait_y_id))


run_nn_classification()
run_knn_classification()
