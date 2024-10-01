from fastapi import APIRouter, HTTPException
from app.business_logic.analyzer import analyze_tone
from app.models.schemas import ToneAnalysisRequest, ToneAnalysisResponse
from app.utils.validators import validate_non_empty_string, validate_string_length
from app.utils.exceptions import ToneValidationError, ToneProcessingError
from app.config.logger import get_logger

# Initialize the logger
logger = get_logger(__name__)

# Initialize the router
router = APIRouter()

@router.post("/analyze", response_model=ToneAnalysisResponse)
async def analyze(request: ToneAnalysisRequest):
    """
    Endpoint to analyze the tone of the provided text.

    This endpoint validates the input text, performs tone analysis using the
    business logic, and returns the detected emotions along with the predominant emotion.
    
    Args:
        request (ToneAnalysisRequest): The request body containing the text to be analyzed.
    
    Returns:
        ToneAnalysisResponse: A response containing the detected emotions, the predominant emotion, 
                              and the confidence percentage.
    
    Raises:
        HTTPException: If validation fails or if any error occurs during tone analysis.
    """
    logger.info(f"Received request to analyze tone: {request.text[:50]}...")

    # Custom validation
    try:
        validate_non_empty_string(request.text)  # Validate that the text is not empty
        validate_string_length(request.text, 500)  # Validate that the text does not exceed 500 characters
    except ToneValidationError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    try:
        # Perform tone analysis
        result = analyze_tone(request.text)
        logger.info(f"Tone analysis successful for text: {request.text[:50]}...")
        return ToneAnalysisResponse(
            emotions=result["emotions"],
            predominant_emotion=result["predominant_emotion"],
            confidence=result["confidence"]
        )
    except ToneProcessingError as e:
        logger.error(f"Processing error: {e}")
        raise HTTPException(status_code=500, detail="Error during tone analysis")
    except Exception as e:
        logger.error(f"Unexpected error during tone analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
