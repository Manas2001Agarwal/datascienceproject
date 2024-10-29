from src.datascience.config.configuration import Configuration_Manager
from src.datascience import logger
from src.datascience.components.data_validation import Data_Validation

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_validation(self):
        config_manager = Configuration_Manager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = Data_Validation(data_validation_config)
        data_validation.save_status_file()
        
if __name__ == "__main__":
    try:
        logger.info(">>>>>>> stage {STAGE_NAME} started >>>>>>")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(">>>>>>> stage {STAGE_NAME} completed >>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e
        