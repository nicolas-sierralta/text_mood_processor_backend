from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuration settings for the Tone Analyzer Service.
    """

    # Application settings
    APP_NAME: str = "Tone Analyzer Service"
    ENVIRONMENT: str
    DEBUG: bool = False  # Set default, will be updated based on ENVIRONMENT

    # Logging settings
    LOGGING_LEVEL: str = "INFO"
    LOG_FILE_PATH: str = "tone_analyzer_service.log"  # <- Este es el campo que falta

    # Inference service settings
    MODEL_INFERENCE_SERVICE_HOST: str
    MODEL_INFERENCE_SERVICE_PORT: int

    model_config = SettingsConfigDict(env_file=".env")

# Create an instance of Settings and update DEBUG based on ENVIRONMENT
settings = Settings()
settings.DEBUG = settings.ENVIRONMENT == "development"