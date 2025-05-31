from datetime import datetime
import logging
import os

# Use safe characters in the filename
LOG_FILE = f"{datetime.now().strftime('%H-%M-%S_%d-%m-%Y')}.log"

# Create logs directory if not exists
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
