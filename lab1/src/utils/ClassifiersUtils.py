from src.classifiers.typedDictionaries.NearestElement import NearestElement


class ClassifiersUtils:
    @staticmethod
    def create_nearest_element(element_id: int, distance: float) -> NearestElement:
        return {
            'element_id': element_id,
            'distance': distance
        }
