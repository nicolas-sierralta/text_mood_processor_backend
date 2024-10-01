from fastapi import APIRouter, HTTPException
from app.business_logic.inference import infer_emotion
from app.models.schemas import InferenceRequest, InferenceResponse
from app.config.logger import get_logger
from app.utils.validators import validate_non_empty_string, validate_string_length
from app.utils.exceptions import InferenceValidationError

# Initialize the logger
logger = get_logger(__name__)

# Initialize the router
router = APIRouter()

@router.post("/inference", response_model=InferenceResponse)
async def inference(request: InferenceRequest):
    """
    Endpoint to perform emotion inference using the model.

    Args:
        request (InferenceRequest): Input text for emotion inference.

    Returns:
        InferenceResponse: The inferred emotions with confidence scores.

    Raises:
        HTTPException: If an error occurs during inference.
    """
    try:
        # Validate input string
        validate_non_empty_string(request.text)
        validate_string_length(request.text, max_length=500)  # Limiting max length of the input text

        result = infer_emotion(request.text)
        logger.info(f"Inference successful for text: {request.text[:50]}...")  # Log first 50 characters
        return InferenceResponse(
            emotions=result["emotions"],
            predominant_emotion=result["predominant_emotion"],
            confidence=result["confidence"]
        )
    except InferenceValidationError as e:
        # Catch validation errors and return a 422 response
        logger.error(f"Inference validation error: {e}")
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error(f"Inference error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during model inference.")