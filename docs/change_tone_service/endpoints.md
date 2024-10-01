# Change Tone Service Endpoints

## Change Tone Endpoint

- **Endpoint**: `/api/change-tone`
- **Method**: POST
- **Description**: Changes the tone of the provided text based on the specified target tone.
- **Request Body**:{"text": "Your text to modify.","target_tone": "desired tone"}
 
**Responses**:

*   **200 OK** : { "original\_text": "Your text to modify.", "modified\_text": "Modified text with the new tone", "applied\_tone": "desired tone"}
    
*   **404 Not Found**: If the change tone resource is not found.
    
*   **409 Conflict**: If there is a conflict during the tone change process.

## Health Check Endpoint

*   **Endpoint**: /health
    
*   **Method**: GET
    
*   **Description**: Returns the status of the Change Tone Service.
    
**Responses**:
    
*   **200 OK**: Returns a message indicating that the Change Tone Service is running.