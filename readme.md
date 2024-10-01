# Text Mood Processor

The **Text Mood Processor** is a powerful API designed to analyze and modify the emotional tone of text inputs. It is built with a microservices architecture and leverages advanced natural language processing techniques and pre-trained models.

- **Documentation**: You can read the full API documentation here: [https://nicolas-sierralta.github.io/text_mood_processor/](https://nicolas-sierralta.github.io/text_mood_processor/)
- **Live Demo**: To see how the API works in action, visit: [https://www.text-mood-processor.live/](https://www.text-mood-processor.live/)

## Overview

The project is composed of the following microservices:

1. **API Gateway**: The central entry point that routes requests to the appropriate services.
2. **Tone Analyzer Service**: Analyzes the emotional tone of the provided text using a pre-trained GoEmotions model.
3. **Change Tone Service**: Changes the tone of the text using OpenAI’s API.
4. **Model Inference Service**: Provides emotion inference on text, powered by the GoEmotions model.

The API offers a range of functionalities for real-time text analysis and modification, making it suitable for applications that need to adapt textual communication dynamically.

## Microservices and Endpoints

### 1. API Gateway

The API Gateway manages requests to the backend services.

- **Endpoint**: `/api/analyze-tone`
  - **Method**: POST
  - **Description**: Analyzes the tone of the provided text.
  - **Request**: `{ "text": "Your text to analyze." }`

- **Endpoint**: `/api/change-tone`
  - **Method**: POST
  - **Description**: Changes the tone of the provided text.
  - **Request**: `{ "text": "Your text", "target_tone": "desired tone" }`

- **Health Check**: `/health`

### 2. Tone Analyzer Service

- **Endpoint**: `/api/inference`
  - **Method**: POST
  - **Description**: Performs emotion inference on the provided text.
  - **Request**: `{ "text": "Your text to analyze." }`

- **Endpoint**: `/api/analyze-tone`
  - **Method**: POST
  - **Description**: Analyzes the tone of the provided text.

- **Health Check**: `/health`

### 3. Change Tone Service

- **Endpoint**: `/api/change-tone`
  - **Method**: POST
  - **Description**: Changes the tone of the text to a specified tone.
  - **Request**: `{ "text": "Your text to modify.", "target_tone": "desired tone" }`

- **Health Check**: `/health`

### 4. Model Inference Service

- **Endpoint**: `/api/inference`
  - **Method**: POST
  - **Description**: Performs emotion inference on the provided text using the GoEmotions model.
  - **Request**: `{ "text": "Your text to analyze." }`

- **Health Check**: `/health`

## Environment Configuration (.env files)

Each microservice is configured using its own `.env` file. Below is an example of the `.env` structure for the different services.

## API Gateway `.env`
- TONE_ANALYZER_URL
- CHANGE_TONE_URL
- LOG_FILE_PATH
- ENVIRONMENT
- DEBUG

## Tone Analyzer Service `.env`
- MODEL_INFERENCE_SERVICE_HOST
- MODEL_INFERENCE_SERVICE_PORT
- LOGGING_LEVEL
- LOG_FILE_PATH
- ENVIRONMENT

## Change Tone Service `.env`
- OPENAI_API_KEY
- OPENAI_MODEL
- MAX_TOKENS
- LOGGING_LEVEL
- LOG_FILE_PATH
- ENVIRONMENT
- DEBUG

## Model Inference Service `.env`
- MODEL_NAME=monologg/bert-base-cased-goemotions-original
- MAX_TOKENS
- LOGGING_LEVEL
- LOG_FILE_PATH
- ENVIRONMENT
- DEBUG


### CI/CD Pipeline
-------

The project uses a CI/CD pipeline with GitHub Actions to build, test, and deploy the microservices. Key features include:

*   **Unit and Integration Tests**: Automatically run tests for each service using pytest.
    
*   **Docker**: Each service is containerized and pushed to GitHub Container Registry.
    
*   **Scaleway Deployment**: Deploys services to a Scaleway server after successful tests.
    
*   **MkDocs**: Documentation can be deployed using MkDocs with the option to trigger it through the workflow\_dispatch event.

### Workflow Dispatch for Documentation Deployment
-------
You can manually trigger the documentation deployment by selecting the mkdocs\_deploy job in GitHub Actions:

      deploy_mkdocs:  
        description: 'Deploy MkDocs documentation?'
        required: false
        default: 'false'
        type: choice
        options:
          - 'true'
          - 'false'

### Running Locally
---------------

To run the project locally, ensure Docker is installed and run the following commands:

- docker-compose up --build

This will start all services defined in docker-compose.yml.

### Testing
-------

Tests are written using pytest. To run the tests:

- pytest --maxfail=1 --disable-warnings

### Documentation
Documentation is created using MkDocs. To serve the documentation locally:

- mkdocs serve

### License
This project is licensed under the MIT License. See the LICENSE file for details.

This README covers an overview of your project, including how to configure it, run it locally, and trigger documentation deployment with GitHub Actions. It also explains the `.env` structure and key CI/CD details. Let me know if you need any further adjustments!