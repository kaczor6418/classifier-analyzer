from typing import List, Dict

import pandas as pd
from sklearn.model_selection import train_test_split

from src.DatasetElement import DatasetElement
from src.FileLoader import FileLoader
from src.converters.ConverterDataFrameToDatasetElement import ConverterDataFrameToDatasetElements


class DataTable:
    leafs_metadata: pd.DataFrame

    chosen_traits: List[int]
    train_dataset: List[DatasetElement] = list()
    test_dataset: List[DatasetElement] = list()
    class_id_with_train_dataset: Dict[int, List[DatasetElement]] = dict()

    def __init__(self, file_path: str, classes_ids: List[int], chosen_traits: List[int]) -> None:
        self.leafs_metadata = FileLoader.load_data_from_csv(file_path)
        self.chosen_traits = chosen_traits;
        self.create_train_and_test_groups(classes_ids)

    def get_leafs_metadata_from_leaf_name_id(self, leaf_name_id: int) -> pd.DataFrame:
        return self.leafs_metadata[self.leafs_metadata[0] == leaf_name_id]

    def create_train_and_test_groups(self, classes_ids: List[int]) -> None:
        every_class_metadata: List[pd.DataFrame] = []
        for class_id in classes_ids:
            class_metadata: pd.DataFrame = self.get_leafs_metadata_from_leaf_name_id(class_id)
            every_class_metadata.append(class_metadata)
            self.class_id_with_train_dataset[class_id] = ConverterDataFrameToDatasetElements.convert(class_metadata)
        train_metadata, test_metadata = train_test_split(pd.concat(every_class_metadata), test_size=0.2,
                                                         random_state=222)
        self.train_dataset = ConverterDataFrameToDatasetElements.convert(train_metadata)
        self.test_dataset = ConverterDataFrameToDatasetElements.convert(test_metadata)
