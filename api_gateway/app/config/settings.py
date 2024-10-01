from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuration settings for the API Gateway.
    """

    # URL for Tone Analyzer Service
    TONE_ANALYZER_URL: str  # Defined in .env
    CHANGE_TONE_URL: str  # Añadir URL para Change Tone Service

    # Logging settings
    LOGGING_LEVEL: str # Defined in .env
    LOGGING_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_FILE_PATH: str = "api_gateway.log"  # Defined en .env o puedes definir un valor por defecto

    # Environment settings
    ENVIRONMENT: str  # Defined in .env
    DEBUG: bool = False  # This will be set based on the environment

    model_config = SettingsConfigDict(env_file=".env")

    # Set DEBUG mode based on the environment
    @property
    def is_debug(self) -> bool:
        """
        Return True if the environment is set to development, otherwise False.
        """
        return self.ENVIRONMENT.lower() == "development"


# Create an instance of Settings
settings = Settings()

