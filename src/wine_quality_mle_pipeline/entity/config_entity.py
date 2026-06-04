from dataclasses import dataclass
from pathlib import Path
from src.wine_quality_mle_pipeline.constants import *
from src.wine_quality_mle_pipeline.utils.common import *
# components-Data Ingestion

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: str



    