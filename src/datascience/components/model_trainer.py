import os
from pathlib import Path
from src.datascience.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import pandas as pd
import joblib

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        train_x = train_data.drop(columns=[self.config.target_columns])
        train_y = train_data[[self.config.target_columns]]
        
        lr = ElasticNet(alpha=self.config.alpha,
                        l1_ratio=self.config.l1_ratio)
        
        lr.fit(train_x,train_y)
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))