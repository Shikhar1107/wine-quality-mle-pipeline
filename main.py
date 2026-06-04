from src.wine_quality_mle_pipeline import logger
from src.wine_quality_mle_pipeline.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<\n\n===================x")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
except Exception as e:
    logger.exception(e)
    raise e