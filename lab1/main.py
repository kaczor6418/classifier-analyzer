import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

csv_file_path = 'leaf/leaf.csv'
leaf_a_name = 'Populus nigra'
leaf_b_name = 'Quercus robur'
trait_a_name = 'Aspect Ratio'
trait_b_name = 'Stochastic Convexity'
leaf_a_id = 3
leaf_b_id = 5
trait_a_id = 4
trait_b_id = 7


def append_element_wit_annotation_to_chart(point, annotation):
    plt.scatter(x=point['x'], y=point['y'], c='green', marker='*')
    plt.annotate(annotation, (point['x'], point['y']))


def count_distance_between_two_points(point_a, point_b):
    return np.sqrt(((point_a['x'] - point_b['x']) ** 2) + ((point_a['y'] - point_b['y']) ** 2))


def classifier_nn(train_group, test_element):
    nearest_element_id_distance = None
    test_element_point = make_a_point_from_leaf_based_on_traits(test_element)
    for train_element in train_group.values:
        train_element_point = make_a_point_from_leaf_based_on_traits(train_element)
        distance = count_distance_between_two_points(test_element_point, train_element_point)
        if nearest_element_id_distance is None:
            nearest_element_id_distance = {
                'id': train_element[0],
                'distance': distance
            }
        else:
            if distance < nearest_element_id_distance['distance']:
                nearest_element_id_distance = {
                    'id': train_element[0],
                    'distance': distance
                }
    return nearest_element_id_distance['id']


def draw_2d_chart(leafs):
    leaf_a_values = get_x_and_y_values_for_leafs(leaf_a_id, leafs)
    leaf_b_values = get_x_and_y_values_for_leafs(leaf_b_id, leafs)
    plt.scatter(x=leaf_a_values['x'], y=leaf_a_values['y'], c='red', marker='s')
    plt.scatter(x=leaf_b_values['x'], y=leaf_b_values['y'], c='blue', marker='^')
    plt.xlabel(trait_a_name)
    plt.ylabel(trait_b_name)
    plt.show()


def get_leaf_by_id(leafs, leaf_id):
    return leafs[leafs[0] == leaf_id]


def get_x_and_y_values_for_leafs(leaf_id, leafs):
    return {
        'x': list(leafs[trait_a_id][leafs[0] == leaf_id]),
        'y': list(leafs[trait_b_id][leafs[0] == leaf_id]),
    }


def load_data_from_csv(path):
    try:
        return pd.read_csv(path, header=None)
    except(FileNotFoundError, pd.errors.EmptyDataError):
        return None


def make_a_point_from_leaf_based_on_traits(leaf):
    return {
        'x': leaf[trait_a_id],
        'y': leaf[trait_b_id]
    }


def run_program():
    leafs_csv = load_data_from_csv(csv_file_path)
    leafs_a = get_leaf_by_id(leafs_csv, leaf_a_id)
    leafs_b = get_leaf_by_id(leafs_csv, leaf_b_id)
    leafs_a_and_b = pd.concat([leafs_a, leafs_b])
    train_leafs, test_leafs = train_test_split(leafs_a_and_b, test_size=0.2, random_state=222)
    for test_leaf in test_leafs.values:
        leaf_name = classifier_nn(train_leafs, test_leaf)
        new_point = make_a_point_from_leaf_based_on_traits(test_leaf)
        if leaf_name == leaf_a_id:
            append_element_wit_annotation_to_chart(new_point, leaf_a_name)
        else:
            append_element_wit_annotation_to_chart(new_point, leaf_b_name)
    draw_2d_chart(train_leafs)


run_program()
