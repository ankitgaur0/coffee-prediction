# logger file is used to define the logging the activity and store in a log named folder 
import os,sys
from datetime import datetime
import logging

log_file=f"{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log"

log_path=os.path.join(os.getcwd(),"Logs","log_file")
os.makedirs(log_path,exist_ok=True)
#log file 
Log_file_path=os.path.join(log_path,log_file)

logging.basicConfig(
    filename=Log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO,
    
)

