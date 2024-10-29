import os
from src.datascience.config.configuration import Configuration_Manager
from src.datascience.components.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config = Configuration_Manager()
        evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(evaluation_config)
        model_evaluation.evaluation()