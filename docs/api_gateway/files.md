# API Gateway Files

## Key Files and Their Responsibilities

- **app/api/routes.py**: Defines the routing for the API, including endpoints for tone analysis and tone modification.
- **app/config/logger.py**: Configures logging for the application, allowing for both console and file logging.
- **app/config/settings.py**: Manages configuration settings, including URLs for microservices and logging preferences.
- **app/services/tone_analyzer_service.py**: Contains the logic to interact with the Tone Analyzer microservice.
- **app/services/change_tone_service.py**: Contains the logic to interact with the Change Tone microservice.
- **app/utils/exceptions.py**: Defines custom exceptions used throughout the API.
- **app/main.py**: Initializes the FastAPI application and includes middleware configurations and health check endpoints.