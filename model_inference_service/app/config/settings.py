from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuration settings for the Model Inference Service.
    """

    # Application settings
    APP_NAME: str = "Model Inference Service"  # <- Se puede definir aquí o en el .env si se necesita
    ENVIRONMENT: str
    DEBUG: bool = False  # Se ajusta según el valor del entorno

    # Logging settings
    LOGGING_LEVEL: str = "INFO"  # <- Definido en el .env
    LOG_FILE_PATH: str = "model_inference_service.log"  # <- Definido en el .env

    # Model settings
    MODEL_NAME: str
    MAX_TOKENS: int

    model_config = SettingsConfigDict(env_file=".env")

# Create an instance of Settings and update DEBUG based on ENVIRONMENT
settings = Settings()
settings.DEBUG = settings.ENVIRONMENT == "development"