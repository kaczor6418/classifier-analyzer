import pandas as pd
from typing import List

from src.structures.DatasetElement import DatasetElement


class ConverterDataFrameDatasetElements:

    @staticmethod
    def to_dataset_elements(df: pd.DataFrame) -> List[DatasetElement]:
        dataset_elements: List[DatasetElement] = []
        for np_array_element in df.values:
            dataset_elements.append(DatasetElement(np_array_element))
        return dataset_elements
