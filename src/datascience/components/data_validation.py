from src.datascience import logger
import os
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd

class Data_Validation:
    def __init__(self,config: DataValidationConfig):
        self.config = config
        
    def validate_data(self):
        data = pd.read_csv(self.config.unzip_data_dir)
        all_cols = list(data.columns)
        
        self.validation_status = None
        
        for col in self.config.all_schema.keys():
            if col in all_cols:
                validation_status = True
            else:
                validation_status = False
                return validation_status
            
        return validation_status
    
    def save_status_file(self):
        validation_status = self.validate_data()
        
        with open(self.config.STATUS_FILE,"w") as file:
            file.write(f"validation_status : {validation_status}")