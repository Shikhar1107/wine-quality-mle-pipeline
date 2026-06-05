from src.wine_quality_mle_pipeline.config.configuration import ConfigurationManager
from src.wine_quality_mle_pipeline.components.data_transformation import DataTransformation
from pathlib import Path

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'),'r') as f:
                status = f.read().split(" ")[-1]
            if status=="True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("You data scheme is not validated")
        except Exception as e:
            raise e