from src.wine_quality_mle_pipeline.config.configuration import ConfigurationManager
from src.wine_quality_mle_pipeline.components.data_ingestion import DataIngestion
from src.wine_quality_mle_pipeline import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
    except Exception as e:
        logger.exception(e)
        raise e