import pandas as pd
from typing import List

from src.Leaf import Leaf


class ConvertDataFrameToLeafs:

    @staticmethod
    def convert(data_frame: pd.DataFrame) -> List[Leaf]:
        leafs: List[Leaf] = []
        for np_array_element in data_frame.values:
            leafs.append(Leaf(np_array_element))
        return leafs
