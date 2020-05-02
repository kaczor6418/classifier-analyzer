from typing import TypedDict, Optional


class ClassificationSchemaDTO(TypedDict):
    type: str
    calculator: str
    k: Optional[int]
