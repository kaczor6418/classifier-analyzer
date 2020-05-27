from typing import TypedDict, List, Optional

from src.analyzer.types.ClassesSchema import ClassSchema
from src.analyzer.types.ClassifiedElementSchema import ClassifiedElementSchema
from src.dto.ClassificationSchemaDTO import ClassificationSchemaDTO


class AnalyzerSchemaDTO(TypedDict):
    csv_file_path: str
    test_group_size: float
    x_axis_trait_id: int
    y_axis_trait_id: int
    traits_ids: List[int]
    classes_config: List[ClassSchema]
    classification_config: ClassificationSchemaDTO
    classified_element_config: Optional[ClassifiedElementSchema]
