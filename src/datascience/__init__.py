import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)
log_filepath = os.path.join(log_dir,"logging.log")

logging.basicConfig(
    format = logging_str,
    level = logging.INFO,
    
    handlers= [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datasciencelogger")