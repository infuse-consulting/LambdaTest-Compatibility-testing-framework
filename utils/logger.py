import logging
import os
from pathlib import Path

def message_logger(log_level=logging.DEBUG):
    root_path = str(Path(__file__).parent.parent)
    logs_dir = f"{root_path}/logs/"
    os.makedirs(logs_dir, exist_ok=True)
    
    logger_name = "Test Logger"
    logger = logging.getLogger(logger_name)
    
    if not logger.handlers:  
        logger.setLevel(log_level)
        file_handler = logging.FileHandler(logs_dir + 'execution.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger

