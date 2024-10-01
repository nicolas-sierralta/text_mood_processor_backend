# Tone Analyzer Service Endpoints


## Inference Endpoint

- **Endpoint**: `/api/inference`
- **Method**: POST
- **Description**: Performs emotion inference on the provided text using the GoEmotions model.

- **Request Body**:{"text": "Your text to analyze."}

**Responses**:

*   **200 OK:**{ "emotions": \[ {"emotion": "joy", "percentage": 75.23}, {"emotion": "sadness", "percentage": 10.12}, {"emotion": "anger", "percentage": 5.00}, {"emotion": "surprise", "percentage": 4.65}, {"emotion": "neutral", "percentage": 5.00} \], "predominant\_emotion": "joy", "confidence": 75.23}
    
*   **422 Unprocessable Entity:**{ "detail": "The value must be a non-empty string."}
    
*   **500 Internal Server Error**{ "detail": "Inference failed: \[error message\]"}

## Analyze Tone Endpoint

- **Endpoint**: `/api/analyze-tone`
- **Method**: POST
- **Description**: Analyzes the tone of the provided text and returns the sentiment analysis results.
- **Request Body**:{"text": "Your text to analyze."}

- **Responses**:

*   **200 OK**:{ "sentiment": "positive", "confidence": 0.95}
    
*   **404 Not Found**: If the tone analysis resource is not found.
    
*   **409 Conflict**: If there is a conflict during analysis.

## Health Check Endpoint

*   **Endpoint**: /health
    
*   **Method**: GET
    
*   **Description**: Returns the status of the Tone Analyzer Service.
    
*   **Responses**:
    
    *   **200 OK**: Returns a message indicating that the Tone Analyzer Service is running.