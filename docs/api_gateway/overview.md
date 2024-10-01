# API Gateway Overview

The API Gateway serves as the entry point for client requests, routing them to the appropriate microservices. It is built with FastAPI and handles requests for tone analysis and tone modification.

## Key Features
- **Routing**: Directs requests to the Tone Analyzer and Change Tone services.
- **Error Handling**: Implements comprehensive error handling for various scenarios.
- **Logging**: Utilizes a logging mechanism to track request processing and errors.
- **Health Check**: Provides a health check endpoint to monitor the API's status.
