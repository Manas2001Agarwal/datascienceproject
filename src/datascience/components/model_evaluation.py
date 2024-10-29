import os
import joblib
import mlflow
import pandas as pd
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.config.configuration import Configuration_Manager
from sklearn.metrics import mean_absolute_error,root_mean_squared_error,r2_score
from src.datascience.utils.common import save_json
from urllib.parse import urlparse
import mlflow.sklearn
from pathlib import Path

os.environ["MLFLOW_TRACKING_USERNAME"]="Manas2001Agarwal"
os.environ["MLFLOW_TRACKING_PASSWORD"]="ea365f2075da53e205158d40f7d0a2c861c30f19"


class ModelEvaluation():
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
        
    def evaluation(self):
        test_data = pd.read_csv(self.config.test_data_path)
        test_x = test_data.drop(columns = [self.config.target_column])
        test_y = test_data[[self.config.target_column]]
        
        model = joblib.load(self.config.model_path)
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        
        with mlflow.start_run():
        
            y_pred = model.predict(test_x)
            rmse,mae,r2 = root_mean_squared_error(test_y,y_pred),mean_absolute_error(test_y,y_pred),r2_score(test_y,y_pred)
            metrics_dict = {
                "rmse" : rmse,
                "mae" : mae,
                "r2" : r2
            }
            save_json(Path(self.config.metrics_file),metrics_dict)
            mlflow.log_metrics(metrics_dict)
            mlflow.log_params(self.config.all_params)
            
            tracking_uri = urlparse(mlflow.get_tracking_uri()).scheme
            if tracking_uri != 'file':
                mlflow.sklearn.log_model(sk_model=model,artifact_path='model',registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(sk_model=model,artifact_path='model')