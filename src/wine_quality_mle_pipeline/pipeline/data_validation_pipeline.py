from src.wine_quality_mle_pipeline import logger
from src.wine_quality_mle_pipeline.components.data_validation import DataValidation
from src.wine_quality_mle_pipeline.config.configuration import ConfigurationManager

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
