# Welcome to the Text Mood Processor API Documentation

The **Text Mood Processor** API is a powerful tool designed to analyze and modify the emotional tone of textual inputs. Utilizing advanced natural language processing techniques and pre-trained models, the API offers various functionalities that enhance text communication for applications.

## Overview

The API consists of multiple microservices that work together to provide a seamless experience for users seeking to analyze and change the tone of their text. Key components of the API include:

- **API Gateway**: Acts as the central entry point for client requests, routing them to the appropriate microservices. It manages the endpoints for tone analysis, tone modification, and health checks, ensuring efficient handling of requests and responses.

- **Inference Service**: Centralizes the loading and management of pre-trained models, such as the GoEmotions model, which is used for emotion inference. This allows for efficient resource usage by avoiding multiple large files.

- **Tone Analyzer Service**: Leverages the Inference Service to analyze the tone of the provided text, returning insights into the emotional states present within the content based on the loaded model.

- **Change Tone Service**: Modifies the tone of the input text using OpenAI's API based on user-defined parameters (e.g., friendly, serious), enabling applications to adapt their communication style effectively.

## Key Features

- **Emotion Analysis**: Identify various emotional states in text, including joy, sadness, anger, and more.

- **Dynamic Tone Modification**: Change the tone of text inputs using OpenAI's API to meet specific communication needs.

- **Real-time Processing**: Offer real-time analysis and modifications for user-generated content.

- **Centralized Model Management**: Efficiently manage model loading through the Inference Service, reducing redundancy and resource consumption.

- **Robust Error Handling**: Implement comprehensive error management to ensure smooth operation and user experience.

- **Detailed Logging**: Track processing steps, model inference requests, and any encountered errors for better monitoring and debugging.

- **Health Check Endpoints**: Verify the operational status of the services to ensure continuous availability.

## Getting Started

To use the Text Mood Processor API, you can interact with the following endpoints:

- **Inference Endpoint**: Perform emotion inference on the input text to understand its emotional context.
- **Tone Analyzer Endpoint**: Analyze the tone of the provided text using the Inference Service.
- **Change Tone Endpoint**: Modify the tone of the input text using OpenAI's API based on specified parameters.
- **Health Check Endpoint**: Check the status of the API services.

For more detailed information about each service and its endpoints, please refer to the corresponding documentation sections.

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project Layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images, and other files.