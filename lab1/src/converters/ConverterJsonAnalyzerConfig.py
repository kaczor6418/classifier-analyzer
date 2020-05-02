from src.analyzer.types.AnalyzerSchema import AnalyzerSchema
from src.analyzer.types.ClassificationSchema import ClassificationSchema
from src.converters.ConvertStringClassifierType import ConverterStringClassifierType
from src.converters.ConverterStringCalculatorType import ConverterStringCalculatorType
from src.dto.AnalyzerSchemaDTO import AnalyzerSchemaDTO
from src.dto.ClassificationSchemaDTO import ClassificationSchemaDTO


class ConverterJsonToAnalyzerConfig:

    @staticmethod
    def to_analyzer_config(json_config: AnalyzerSchemaDTO) -> AnalyzerSchema:
        converted: AnalyzerSchema = dict()
        converted['csv_file_path'] = json_config['csv_file_path']
        converted['test_group_size'] = json_config['test_group_size']
        converted['x_axis_trait_id'] = json_config['x_axis_trait_id']
        converted['y_axis_trait_id'] = json_config['y_axis_trait_id']
        converted['traits_ids'] = json_config['traits_ids']
        converted['classes_config'] = json_config['classes_config']
        converted['classification_config'] = ConverterJsonToAnalyzerConfig.to_classification_config(
            json_config['classification_config'])
        if 'classified_element_config' in json_config:
            converted['classified_element_config'] = json_config['classified_element_config']
        else:
            converted['classified_element_config'] = dict()
            converted['classified_element_config']['point_color'] = 'green'
            converted['classified_element_config']['point_marker'] = '*'
        return converted

    @staticmethod
    def to_classification_config(json_config: ClassificationSchemaDTO) -> ClassificationSchema:
        converted: ClassificationSchema = dict()
        converted['type'] = ConverterStringClassifierType.to_enum(json_config['type'])
        converted['calculator'] = ConverterStringCalculatorType.to_enum(json_config['calculator'])
        if 'k' in json_config:
            converted['k'] = json_config['k']
        return converted
