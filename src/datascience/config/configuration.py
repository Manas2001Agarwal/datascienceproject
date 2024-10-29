from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience.entity.config_entity import DataTransformationConfig
from src.datascience.entity.config_entity import ModelTrainerConfig
from src.datascience.entity.config_entity import ModelEvaluationConfig
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
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir])
        
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            test_data_path = config.test_data_path,
            train_data_path = config.train_data_path,
            model_name = config.model_name,
            l1_ratio = params.l1_ratio,
            alpha = params.alpha,
            target_columns = schema.name
        )
        
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metrics_file=config.metrics_file,
            mlflow_uri = "https://dagshub.com/Manas2001Agarwal/datascienceproject.mlflow", 
            target_column=schema.name
        )
        
        return model_evaluation_config
        
        