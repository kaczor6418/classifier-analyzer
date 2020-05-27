from typing import TypeVar, Dict, List

T = TypeVar('T')
V = TypeVar('V')


class Utils:

    @staticmethod
    def get_key_value_by_id_from_dictionaries(dictionaries: List[Dict[T, V]], id_value: V, key: T) -> V:
        for dictionary in dictionaries:
            if dictionary['id'] == id_value:
                return dictionary.get(key)
