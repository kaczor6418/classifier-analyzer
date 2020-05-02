import sys

import pandas as pd


class CsvFileLoader:

    @staticmethod
    def load_file(path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(path, header=None)
        except(FileNotFoundError, pd.errors.EmptyDataError):
            sys.exit('Can not load csv file')
