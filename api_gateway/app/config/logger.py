import logging
import os

# Retrieve logging settings from environment variables or use defaults
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO").upper()
LOGGING_FORMAT = os.getenv("LOGGING_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "api_gateway.log")

# Configure logging settings
logging.basicConfig(
    level=LOGGING_LEVEL,
    format=LOGGING_FORMAT,
    handlers=[
        logging.StreamHandler(),  # Logs to the console
        logging.FileHandler(LOG_FILE_PATH),  # Logs to a file
    ]
)

# Create a logger instance
def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger instance for the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """
    return logging.getLogger(name)
