import os
import logging
from datetime import datetime


LOG_DIR = "Logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = f"Log_{datetime.now().strftime('%Y%m%D%H%M%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)


logging.basicConfig(
    filename=LOG_PATH,
    format="[%(asctime)s]-%(levelname)s-%(message)s",
    level= logging.INFO,
    force = True
) 

logger = logging.getLogger()