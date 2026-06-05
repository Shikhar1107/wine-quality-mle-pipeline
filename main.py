from src.wine_quality_mle_pipeline import logger
from src.wine_quality_mle_pipeline.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wine_quality_mle_pipeline.pipeline.data_validation_pipeline import DataValidationPipeline
from src.wine_quality_mle_pipeline.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.wine_quality_mle_pipeline.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.wine_quality_mle_pipeline.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<\n\n===================x")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<\n\n===================x")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<\n\n===================x")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<\n\n===================x")
    obj = ModelTrainerPipeline()
    obj.initiate_model_training()
except Exception as e:
    logger.excpetion(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<\n\n===================x")
    obj = ModelEvaluationPipeline()
    obj.inititate_model_eval()
except Exception as e:
    logger.exception(e)
    raise e

