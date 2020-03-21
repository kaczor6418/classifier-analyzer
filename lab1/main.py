import matplotlib.pyplot as plt
import pandas as pd
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


def load_data_from_csv(path):
    try:
        return pd.read_csv(path, header=None)
    except(FileNotFoundError, pd.errors.EmptyDataError):
        return None


def get_leaf_by_id(leafs, leaf_id):
    return leafs[leafs[0] == leaf_id]


def get_two_leafs(leafs):
    return leafs[(leafs[0] == leaf_a_id) | (leafs[0] == leaf_b_id)]


def get_x_and_y_values_for_leafs(leaf_id, leafs):
    return {
        'x': list(leafs[trait_a_id][leafs[0] == leaf_id]),
        'y': list(leafs[trait_b_id][leafs[0] == leaf_id]),
    }


def draw_2d_chart(leafs):
    leaf_a_values = get_x_and_y_values_for_leafs(leaf_a_id, leafs)
    leaf_b_values = get_x_and_y_values_for_leafs(leaf_b_id, leafs)
    plt.scatter(x=leaf_a_values['x'], y=leaf_a_values['y'], c='red')
    plt.scatter(x=leaf_b_values['x'], y=leaf_b_values['y'], c='blue')
    plt.xlabel(trait_a_name)
    plt.ylabel(trait_b_name)
    plt.show()


leafs_csv = load_data_from_csv(csv_file_path)
leafs_a = get_leaf_by_id(leafs_csv, leaf_a_id)
leafs_b = get_leaf_by_id(leafs_csv, leaf_b_id)
ll = get_two_leafs(leafs_csv)
print(leafs_a + leafs_b)
print('----------------------------------')
print(ll)
train_leafs, test_leafs = train_test_split(ll, test_size=0.2, random_state=222)
draw_2d_chart(train_leafs)
