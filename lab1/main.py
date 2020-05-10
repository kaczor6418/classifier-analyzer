from src.analyzer.Analyzer import Analyzer
from src.analyzer.types.AnalyzerSchema import AnalyzerSchema
from src.converters.ConverterJsonAnalyzerConfig import ConverterJsonToAnalyzerConfig
from src.dto.AnalyzerSchemaDTO import AnalyzerSchemaDTO
from src.loaders.JsonFileLodaer import JsonFileLoader


def create_analysis(config_path: str) -> None:
    json_config: AnalyzerSchemaDTO = JsonFileLoader.load_file(config_path)
    converted_config: AnalyzerSchema = ConverterJsonToAnalyzerConfig.to_analyzer_config(json_config)
    analyzer: Analyzer = Analyzer(converted_config)
    analyzer.run_analysis()
    analyzer.show_results()


create_analysis('config/cfg-nn-euclides-class=[3,5,7]-traits=[all].json')
create_analysis('config/cfg-knn-euclides-k=3-class=[3,5,7]-traits=[all].json')
create_analysis('config/cfg-nm-euclides-class=[3,5,7]-traits=[all].json')
create_analysis('config/cfg-nn-deviation-class=[3,5,7]-traits=[all].json')
create_analysis('config/cfg-knn-deviation-k=3-class=[3,5,7]-traits=[all].json')
create_analysis('config/cfg-nm-deviation-class=[3,5,7]-traits=[all].json')
