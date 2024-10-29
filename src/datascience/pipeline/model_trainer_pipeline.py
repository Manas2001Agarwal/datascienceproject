import os
from src.datascience.config.configuration import Configuration_Manager
from src.datascience.components.model_trainer import ModelTrainer

class ModelTrainerTrainingPipeline:
    
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = Configuration_Manager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()