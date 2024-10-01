import requests
from app.config.logger import get_logger
from app.config.settings import settings
from app.utils.validators import validate_non_empty_string
from app.utils.exceptions import ToneValidationError, ToneProcessingError

# Create a logger for this module
logger = get_logger(__name__)

INFERENCE_SERVICE_URL = f"http://{settings.MODEL_INFERENCE_SERVICE_HOST}:{settings.MODEL_INFERENCE_SERVICE_PORT}/api/inference"

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text before sending it to the inference service.
    """
    validate_non_empty_string(text)  # Validate input
    processed_text = text.lower().strip()  # Lowercase and strip whitespace
    logger.debug(f"Preprocessed text: {processed_text}")
    return processed_text

def postprocess_results(results: dict) -> dict:
    """
    Postprocess the results from the inference service.
    """
    if results["confidence"] < 50:
        results["message"] = "Low confidence in the predominant emotion."
    else:
        results["message"] = "Tone analysis successful with high confidence."
    
    logger.debug(f"Postprocessed results: {results}")
    return results

def analyze_tone(text: str) -> dict:
    """
    Analyze the tone of the input text using the inference service.
    """
    try:
        # Preprocess the text
        preprocessed_text = preprocess_text(text)

        # Send a request to the inference service
        logger.info(f"Calling inference service at {INFERENCE_SERVICE_URL}")
        response = requests.post(INFERENCE_SERVICE_URL, json={"text": preprocessed_text})

        if response.status_code != 200:
            logger.error(f"Inference service returned an error: {response.status_code}")
            raise ToneProcessingError(f"Inference service error: {response.status_code}")

        # Postprocess the inference results
        inference_results = response.json()
        logger.info(f"Inference service returned: {inference_results}")
        return postprocess_results(inference_results)

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error during tone analysis: {e}")
        raise ToneProcessingError(f"Failed to connect to inference service: {e}")
    except ToneValidationError as e:
        logger.error(f"Validation error: {e}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error during tone analysis: {e}")
        raise ToneProcessingError(f"Error during tone analysis: {e}")