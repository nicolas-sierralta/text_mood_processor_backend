import pytest
from app.business_logic.inference import infer_emotion
from app.utils.exceptions import InferenceValidationError

def test_infer_emotion_valid_text():
    """
    Test valid text inference.
    """
    text = "I am very happy today!"
    result = infer_emotion(text)
    assert "emotions" in result
    assert "predominant_emotion" in result
    assert "confidence" in result
    assert len(result["emotions"]) > 0  # Ensure there are emotions in the response
    assert result["confidence"] > 0  # Ensure confidence is a positive number

def test_infer_emotion_empty_text():
    """
    Test inference with empty text (expect InferenceValidationError).
    """
    text = ""
    with pytest.raises(InferenceValidationError):
        infer_emotion(text)

def test_infer_emotion_handles_long_text():
    """
    Test inference with long text (ensure it doesn't fail or truncate excessively).
    """
    text = "This is a very long text. " * 100
    result = infer_emotion(text)
    assert "emotions" in result
    assert len(result["emotions"]) > 0  # Ensure emotions are returned
    assert result["confidence"] > 0  # Ensure confidence is valid

