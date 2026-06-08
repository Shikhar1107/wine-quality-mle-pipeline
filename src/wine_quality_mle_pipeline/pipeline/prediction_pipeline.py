import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from src.wine_quality_mle_pipeline.constants import *
from src.wine_quality_mle_pipeline.utils.common import *

config_filepath=CONFIG_FILE_PATH
config_file = read_yaml(config_filepath)
config = config_file.prediction

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path(config.model_path))

    def predict(self,data):
        prediction = self.model.predict(data)
        return prediction
