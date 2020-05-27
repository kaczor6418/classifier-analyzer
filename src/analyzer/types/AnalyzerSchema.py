from typing import TypedDict, List

from src.analyzer.types.ClassesSchema import ClassSchema
from src.analyzer.types.ClassificationSchema import ClassificationSchema
from src.analyzer.types.ClassifiedElementSchema import ClassifiedElementSchema


class AnalyzerSchema(TypedDict):
    csv_file_path: str
    test_group_size: float
    x_axis_trait_id: int
    y_axis_trait_id: int
    traits_ids: List[int]
    classes_config: List[ClassSchema]
    classification_config: ClassificationSchema
    classified_element_config: ClassifiedElementSchema
