from src.datascience.config.configuration import Configuration_Manager
from src.datascience import logger
from src.datascience.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        config = Configuration_Manager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download()
        data_ingestion.extract_zip_file()
        
if __name__ == "__main__":
    try:
        logger.info(">>>>>>> stage {STAGE_NAME} started >>>>>>")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(">>>>>>> stage {STAGE_NAME} completed >>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e
        