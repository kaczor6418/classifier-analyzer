from src.analyzer.Analyzer import Analyzer
from src.analyzer.types.AnalyzerSchema import AnalyzerSchema
from src.converters.ConverterJsonAnalyzerConfig import ConverterJsonToAnalyzerConfig
from src.dto.AnalyzerSchemaDTO import AnalyzerSchemaDTO
from src.loaders.JsonFileLodaer import JsonFileLoader

json_config: AnalyzerSchemaDTO = JsonFileLoader.load_file('configs/cfg-knn-euclides-k=3-class=[3,5]-traits=[4,7].json')
converted_config: AnalyzerSchema = ConverterJsonToAnalyzerConfig.to_analyzer_config(json_config)
analyzer: Analyzer = Analyzer(converted_config)
analyzer.run_analysis()
