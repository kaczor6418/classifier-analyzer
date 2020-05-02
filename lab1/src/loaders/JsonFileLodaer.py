import json
import sys


class JsonFileLoader:

    @staticmethod
    def load_file(path: str) -> dict:
        try:
            with open(path) as json_file:
                return json.load(json_file)
        except(FileNotFoundError, json.JSONDecodeError):
            sys.exit('Can not load json file')
