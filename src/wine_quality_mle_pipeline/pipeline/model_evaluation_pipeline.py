from src.wine_quality_mle_pipeline import logger
from src.wine_quality_mle_pipeline.components.model_evaluation import ModelEvaluation
from src.wine_quality_mle_pipeline.config.configuration import ConfigurationManager

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def inititate_model_eval(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
        print("Model Evaluation completed!!")