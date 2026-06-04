import os
import yaml
from src.wine_quality_mle_pipeline import logger
import json
import joblib
from beartype import beartype
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError

@beartype
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    read yaml file and returns

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"ymal file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
@beartype
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories
    Args:
    path_to_directories (list): list of path of directories
    ignore_log (bool, optional): ignore if multiple dir is to be created. Defaults to False
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok= True)
        if verbose:
            logger.info(f"created directory at: {path}")

@beartype
def save_json(path: Path, data: dict):
    """
    save json data

    Args: 
    path (Path): path to json file
    data(dict): data to be saved in your json file
    """

    with open(path,'w') as f:
        json.dump(data, f ,indent=4)
    
    logger.info(f"json file saved at: {path}")

@beartype
def load_json(path:Path)->ConfigBox:
    """
    loads json files data

    Args:
    path (Path): path to json file

    Returns:
        ConfigBox : data as class attributes instead of dict
    """

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@beartype
def save_bin(data: Any, path: Path):
    """save binary file
    
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data,filename=data)
    logger.info(f"binary file saved at: {path}")

@beartype
def load_bin(path: Path) -> Any:
    """
    Load binary data

    Args:
    path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data= joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data