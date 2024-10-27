import os
import joblib
import yaml
import json
from src.datascience import logger
from box import ConfigBox
from pathlib import Path
from ensure import ensure_annotations
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_file:Path) -> ConfigBox:
    content = yaml.safe_load(open(path_to_file,"r"))
    logger.info(f"yaml file at {path_to_file} loaded successfully")
    return ConfigBox(content)

@ensure_annotations
def create_directories(path_to_directory:list,verbose=True):
    for dir_path in path_to_directory:
        os.makedirs(dir_path,exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {dir_path}")
            
@ensure_annotations
def save_json(path_to_json:Path,data:dict):
    with open(path_to_json,"w") as json_file:
        json.dump(data,json_file,indent=4)
    logger.info(f"JSON at path {path_to_json} saved")      

@ensure_annotations        
def load_json(path_to_json:Path) -> ConfigBox:
    with open(path_to_json,"r") as json_file:
       content =  json.load(json_file)
    
    logger.info(f"JSON at path {path_to_json} loaded")   
    return ConfigBox(json_file)

@ensure_annotations 
def save_model(model:Any,path_to_model:Path):
    joblib.dump(value=model,filename=path_to_model)
    logger.info(f"Model path {path_to_model} saved") 

@ensure_annotations     
def load_model(path_to_model:Path) -> Any:
    model = joblib.load(path_to_model) 
    logger.info(f"Model loaded from {path_to_model}") 
    return model