from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience.entity.config_entity import DataValidationConfig
import os
from src.datascience.utils.common import read_yaml, create_directories 
from src.datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH


class Configuration_Manager:
    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        create_directories([self.config.data_ingestion.root_dir])
        config = self.config.data_ingestion
        
        data_ingestion = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        create_directories([self.config.data_validation.root_dir])
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        data_validation = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema = schema
        )      
        return data_validation   