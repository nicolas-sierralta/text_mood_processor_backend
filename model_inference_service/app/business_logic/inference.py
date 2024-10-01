from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from app.config.logger import get_logger
from app.utils.exceptions import InferenceValidationError, ModelLoadingError, InferenceRuntimeError
from app.utils.validators import validate_non_empty_string

# Initialize the logger
logger = get_logger(__name__)

# Define the emotions from the GoEmotions model
EMOTIONS = [
    "admiration", "amusement", "anger", "annoyance", "approval", "caring", "confusion", "curiosity",
    "desire", "disappointment", "disapproval", "disgust", "embarrassment", "excitement", "fear", "gratitude",
    "grief", "joy", "love", "nervousness", "optimism", "pride", "realization", "relief", "remorse", "sadness",
    "surprise", "neutral"
]

# Load the GoEmotions model and tokenizer
try:
    # Load tokenizer and model from pre-trained GoEmotions model
    tokenizer = AutoTokenizer.from_pretrained("monologg/bert-base-cased-goemotions-original", clean_up_tokenization_spaces=True)
    model = AutoModelForSequenceClassification.from_pretrained("monologg/bert-base-cased-goemotions-original")
    logger.info("GoEmotions model loaded successfully.")
except Exception as e:
    logger.error("Failed to load GoEmotions model: %s", str(e))
    raise ModelLoadingError(f"Failed to load model: {str(e)}")

def infer_emotion(text: str) -> dict:
    """
    Perform emotion inference using the GoEmotions model with the provided text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary containing detected emotions and their respective scores.

    Raises:
        InferenceValidationError: If the input text is invalid.
        InferenceRuntimeError: If an unexpected error occurs during inference.
    """
    # Validate the input string
    validate_non_empty_string(text)

    try:
        logger.info(f"Performing inference on text: {text[:100]}...")  # Log only the first 100 characters

        # Tokenize the input text
        inputs = tokenizer([text], return_tensors="pt", padding=True, truncation=True)

        # Perform inference using the model
        outputs = model(**inputs)

        # Apply softmax to get emotion scores
        scores = torch.nn.functional.softmax(outputs.logits, dim=1)

        # Sort emotions by their scores in descending order
        sorted_scores, indices = torch.sort(scores, descending=True)

        # Create a list of emotions and their corresponding percentages
        top_emotions = [
            {"emotion": EMOTIONS[idx], "percentage": round(score.item() * 100, 2)}
            for idx, score in zip(indices[0], sorted_scores[0])
        ]

        # Return the top 5 emotions and the predominant emotion with confidence score
        return {
            "emotions": top_emotions[:5],  # Limit to top 5 emotions
            "predominant_emotion": top_emotions[0]["emotion"],
            "confidence": top_emotions[0]["percentage"]
        }

    except Exception as e:
        logger.error(f"Error during inference: {e}")
        raise InferenceRuntimeError(f"Inference failed: {str(e)}")
