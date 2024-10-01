import logging
import os

# Retrieve logging settings from environment variables
LOGGING_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOGGING_FORMAT = os.getenv("LOGGING_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "tone_analyzer_service.log")

# Configure logging
logging.basicConfig(
    level=LOGGING_LEVEL,
    format=LOGGING_FORMAT,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE_PATH),
    ]
)

def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger instance with the specified name.
    """
    return logging.getLogger(name)
