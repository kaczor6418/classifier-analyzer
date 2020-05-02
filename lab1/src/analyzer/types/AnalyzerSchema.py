from typing import TypedDict, List, Union, Optional

from src.analyzer.types.ClassesSchema import ClassSchema
from src.analyzer.types.ClassificationSchema import NNClassification, KNNClassification
from src.analyzer.types.ClassifiedElementSchema import ClassifiedElementSchema


class AnalyzerSchema(TypedDict):
    csv_file_path: str
    test_group_size: int
    x_axis_trait_id: int
    y_axis_trait_id: int
    traits_ids: List[int]
    classes_config: List[ClassSchema]
    classification_config: Union[NNClassification, KNNClassification]
    classified_element_config: Optional[ClassifiedElementSchema]
