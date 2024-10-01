from pydantic_settings import BaseSettings, SettingsConfigDict

class ChangeToneSettings(BaseSettings):
    """
    Configuration settings for the Change Tone Service.
    
    This class loads and manages all configuration options for the Change Tone Service, 
    including application settings, logging settings, and OpenAI API settings. 
    The values are typically loaded from a .env file.
    """

    # Application settings
    APP_NAME: str = "Change Tone Service"  # The name of the application
    DEBUG: bool = False  # Debug mode flag, default is False but can be set in .env

    # Logging settings
    LOGGING_LEVEL: str  # The logging level (e.g., DEBUG, INFO) defined in the .env file
    LOG_FILE_PATH: str = "change_tone_service.log"  # Default log file path, can be overridden in .env

    # OpenAI API settings
    OPENAI_API_KEY: str  # The API key for OpenAI, required and defined in .env
    OPENAI_MODEL: str  # The OpenAI model to use, defined in .env (e.g., "gpt-3.5-turbo")
    MAX_TOKENS: int  # The maximum number of tokens allowed for the OpenAI API, defined in .env
    ENVIRONMENT: str
    
    # Specify the .env file to load configuration from
    model_config = SettingsConfigDict(env_file=".env")

# Create an instance of ChangeToneSettings and update DEBUG based on ENVIRONMENT
change_tone_settings = ChangeToneSettings()

# Set the DEBUG mode based on the environment; activate if ENVIRONMENT is "development"
change_tone_settings.DEBUG = change_tone_settings.ENVIRONMENT == "development"
