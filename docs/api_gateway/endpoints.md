# API Gateway Endpoints

## Analyze Tone Endpoint

- **Endpoint**: `/api/analyze-tone`
- **Method**: POST
- **Description**: Analyzes the tone of the provided text.
- **Request Body**:{"text": "Your text to analyze."}

**Responses**:

*   **200 OK**: Returns the analysis result.
    
*   **404 Not Found**: If the tone analysis resource is not found.
    
*   **409 Conflict**: If there is a conflict during analysis.

## Change Tone Endpoint


*   **Endpoint**: /api/change-tone
    
*   **Method**: POST
    
*   **Description**: Changes the tone of the provided text based on the specified target tone.
    
*   **Request Body**: { "text": "Your text to modify.", "target\_tone": "desired tone"}
    
*   **Responses**:
    
    *   **200 OK**: Returns the modified text.
        
    *   **404 Not Found**: If the change tone resource is not found.
        
    *   **409 Conflict**: If there is a conflict during the tone change process.

# Health Check Endpoint


*   **Endpoint**: /health
    
*   **Method**: GET
    
*   **Description**: Returns the status of the API Gateway.
    
*   **Responses**:
    
    *   **200 OK**: Returns a message indicating that the API Gateway is running.