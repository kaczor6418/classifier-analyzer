from typing import List

import pandas as pd
from sklearn.model_selection import train_test_split

from src.FileLoader import FileLoader
from src.DatasetElement import DatasetElement
from src.converters.ConverterDataFrameToDatasetElement import ConverterDataFrameToDatasetElements


class DataTable:
    leaf_a_id: int
    leaf_b_id: int
    trait_x_id: int
    trait_y_id: int

    leafs_metadata: pd.DataFrame
    leafs_a_metadata: pd.DataFrame
    leafs_b_metadata: pd.DataFrame

    train_leafs: List[DatasetElement]
    train_leafs_a: List[DatasetElement]
    train_leafs_b: List[DatasetElement]
    test_leafs: List[DatasetElement]

    def __init__(self, file_path: str, leaf_a_id: int, leaf_b_id: int, trait_x_id: int, trait_y_id) -> None:
        self.leaf_a_id = leaf_a_id
        self.leaf_b_id = leaf_b_id
        self.trait_x_id = trait_x_id
        self.trait_y_id = trait_y_id
        self.leafs_metadata = FileLoader.load_data_from_csv(file_path)
        self.leafs_a_metadata = self.get_leafs_metadata_from_leaf_name_id(self.leaf_a_id)
        self.leafs_b_metadata = self.get_leafs_metadata_from_leaf_name_id(self.leaf_b_id)
        self.create_train_and_test_leafs()

    def get_leafs_metadata_from_leaf_name_id(self, leaf_name_id: int) -> pd.DataFrame:
        return self.leafs_metadata[self.leafs_metadata[0] == leaf_name_id]

    def create_train_and_test_leafs(self) -> None:
        leafs_a_b_metadata: pd.DataFrame = pd.concat([self.leafs_a_metadata, self.leafs_b_metadata])
        train_leafs_metadata, test_leafs_metadata = train_test_split(leafs_a_b_metadata, test_size=0.2,
                                                                     random_state=222)
        self.train_leafs = ConverterDataFrameToDatasetElements.convert(train_leafs_metadata)
        self.test_leafs = ConverterDataFrameToDatasetElements.convert(test_leafs_metadata)
        train_leafs_a_metadata = self.get_leafs_metadata_from_leaf_name_id(self.leaf_a_id)
        train_leafs_b_metadata = self.get_leafs_metadata_from_leaf_name_id(self.leaf_b_id)
        self.train_leafs_a = ConverterDataFrameToDatasetElements.convert(train_leafs_a_metadata)
        self.train_leafs_b = ConverterDataFrameToDatasetElements.convert(train_leafs_b_metadata)
