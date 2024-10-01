from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException
from app.services.tone_analyzer_service import tone_analyzer_service
from app.services.change_tone_service import change_tone_service 
from app.config.logger import get_logger
from app.utils.exceptions import ValidationError, NotFoundError, ConflictError

# Instantiate the logger using get_logger
logger = get_logger(__name__)

class AnalyzeToneRequest(BaseModel):
    """
    Schema for tone analysis request.
    """
    text: str = Field(
        ..., 
        min_length=1, 
        max_length=2000,  # Limit input text to 2000 characters
        description="Text to analyze. Cannot be empty or exceed 2000 characters."
    )

class ChangeToneRequest(BaseModel):
    """
    Schema for change tone request.
    """
    text: str = Field(
        ..., 
        min_length=1, 
        max_length=2000,  # Limit input text to 2000 characters
        description="Text to modify. Cannot be empty or exceed 2000 characters."
    )
    target_tone: str = Field(
        ..., 
        min_length=1,
        description="Target tone to apply to the text."
    )

# Initialize the router
router = APIRouter()

@router.post("/analyze-tone", summary="Analyze the tone of the input text")
async def analyze_tone(request: AnalyzeToneRequest):
    """
    Endpoint to analyze the tone of a given text.

    Args:
        request (AnalyzeToneRequest): The input text to analyze.

    Returns:
        dict: The result of the tone analysis.

    Raises:
        ValidationError: If the input text is empty or invalid.
        NotFoundError: If the tone analysis resource could not be found.
        ConflictError: If a conflict occurs during the tone analysis.
        HTTPException: For any other unexpected errors.
    """
    logger.info("Received request to analyze tone")

    try:
        result = await tone_analyzer_service.analyze_tone(request.text)
        logger.info("Tone analysis completed successfully")
        return result

    except NotFoundError as not_found_exc:
        logger.error(f"Tone analysis resource not found: {not_found_exc.detail}")
        raise HTTPException(status_code=404, detail=str(not_found_exc))

    except ConflictError as conflict_exc:
        logger.error(f"Conflict during tone analysis: {conflict_exc.detail}")
        raise HTTPException(status_code=409, detail=str(conflict_exc))

    except HTTPException as http_exc:
        logger.error(f"HTTP error during tone analysis: {http_exc.detail}")
        raise http_exc

    except Exception as e:
        logger.error(f"Unexpected error during tone analysis: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/change-tone", summary="Change the tone of the input text")
async def change_tone(request: ChangeToneRequest):
    """
    Endpoint to change the tone of a given text.

    Args:
        request (ChangeToneRequest): The input text to modify and the target tone.

    Returns:
        dict: The result of the tone modification.

    Raises:
        ValidationError: If the input text or target tone is invalid.
        NotFoundError: If the change tone resource could not be found.
        ConflictError: If a conflict occurs during the tone change.
        HTTPException: For any other unexpected errors.
    """
    logger.info("Received request to change tone")

    try:
        result = await change_tone_service.change_tone(request.text, request.target_tone)
        logger.info("Tone change completed successfully")
        return result

    except NotFoundError as not_found_exc:
        logger.error(f"Change tone resource not found: {not_found_exc.detail}")
        raise HTTPException(status_code=404, detail=str(not_found_exc))

    except ConflictError as conflict_exc:
        logger.error(f"Conflict during tone change: {conflict_exc.detail}")
        raise HTTPException(status_code=409, detail=str(conflict_exc))

    except HTTPException as http_exc:
        logger.error(f"HTTP error during tone change: {http_exc.detail}")
        raise http_exc

    except Exception as e:
        logger.error(f"Unexpected error during tone change: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")