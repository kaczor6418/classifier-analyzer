from typing import TypedDict, List, Union, Optional

from src.analyzer.typedDictionaries.ClassesConfig import ClassConfig
from src.analyzer.typedDictionaries.ClassificationConfig import NNClassification, KNNClassification
from src.analyzer.typedDictionaries.ClassyfiedElementConfig import ClassifiedElementConfig


class AnalyzerConfig(TypedDict):
    csv_file_path: str
    test_group_size: int
    x_axis_trait_id: int
    y_axis_trait_id: int
    traits_ids: List[int]
    classes_config: List[ClassConfig]
    classification_config: Union[NNClassification, KNNClassification]
    classified_element_config: Optional[ClassifiedElementConfig]
