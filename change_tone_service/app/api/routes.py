from fastapi import APIRouter, HTTPException
from app.business_logic.change_tone import change_tone  
from app.models.schemas import ChangeToneRequest, ChangeToneResponse
from app.config.logger import get_logger
from app.utils.validators import validate_non_empty_string, validate_string_length
from app.utils.exceptions import ChangeToneValidationError

# Instantiate the logger using get_logger
logger = get_logger(__name__)

# Initialize the router
router = APIRouter()

@router.post("/change-tone", response_model=ChangeToneResponse)
async def change_tone_endpoint(request: ChangeToneRequest):
    """
    Endpoint to change the tone of a given text.

    This endpoint accepts a text and a target tone, validates them, and 
    then calls the business logic to apply the tone change.

    Args:
        request (ChangeToneRequest): The input text and target tone provided by the user.

    Returns:
        ChangeToneResponse: A response containing the original text, modified text, and the applied tone.

    Raises:
        HTTPException: 
            - 422 if validation fails.
            - 500 if any unexpected error occurs during tone change.
    """
    try:
        # Validate the input text and the target tone
        validate_non_empty_string(request.text)  # Ensure the text is not empty
        validate_string_length(request.text, max_length=500)  # Ensure the text does not exceed 500 characters
        validate_non_empty_string(request.target_tone)  # Ensure the target tone is not empty

        # Call the business logic to apply the tone change
        result = change_tone(request.text, request.target_tone)
        
        # Log the success of the tone change operation
        logger.info(f"Tone change successful for text: {request.text[:50]}... to tone: {request.target_tone}")
        
        # Return the response with the original and modified text
        return ChangeToneResponse(
            original_text=result["original_text"],
            modified_text=result["modified_text"],
            applied_tone=result["applied_tone"]
        )
    
    except ChangeToneValidationError as e:
        # Handle validation errors specific to tone change
        logger.error(f"Change tone validation error: {e}")
        raise HTTPException(status_code=422, detail=str(e))
    
    except Exception as e:
        # Handle any unexpected errors during tone change
        logger.error(f"Change tone error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during tone change.") 
