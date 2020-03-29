import pandas as pd


class FileLoader:

    @staticmethod
    def load_data_from_csv(path) -> pd.DataFrame:
        try:
            return pd.read_csv(path, header=None)
        except(FileNotFoundError, pd.errors.EmptyDataError):
            print('Can not load csv file')
