import pandas as pd
from typing import List

from src.Leaf import Leaf


class ConvertDataFrameToLeafs:

    @staticmethod
    def convert(df: pd.DataFrame) -> List[Leaf]:
        leafs: List[Leaf] = []
        for np_array_element in df.values:
            leafs.append(Leaf(np_array_element))
        return leafs
