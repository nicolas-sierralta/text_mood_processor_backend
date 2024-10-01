import pytest
import requests_mock
from app.business_logic.analyzer import analyze_tone
from app.utils.exceptions import ToneValidationError, ToneProcessingError

# Mock the inference service URL for the tests
INFERENCE_SERVICE_URL = "http://model_inference_service:8001/api/inference"

def test_analyze_tone_valid_response():
    """
    Test that analyze_tone returns correct results when the inference service gives a valid response.
    """
    with requests_mock.Mocker() as mock:
        mock.post(INFERENCE_SERVICE_URL, json={
            "emotions": [
                {"emotion": "joy", "percentage": 80.0},
                {"emotion": "neutral", "percentage": 20.0}
            ],
            "predominant_emotion": "joy",
            "confidence": 80.0
        }, status_code=200)

        result = analyze_tone("I am happy today!")
        
        assert "emotions" in result
        assert result["predominant_emotion"] == "joy"
        assert result["confidence"] == 80.0
        assert result["message"] == "Tone analysis successful with high confidence."


def test_analyze_tone_inference_service_error():
    """
    Test that analyze_tone raises a ToneProcessingError when the inference service returns an error.
    """
    with requests_mock.Mocker() as mock:
        mock.post(INFERENCE_SERVICE_URL, status_code=500)

        with pytest.raises(ToneProcessingError) as exc_info:
            analyze_tone("This will fail!")
        
        assert "Inference service error: 500" in str(exc_info.value)


def test_analyze_tone_empty_text():
    """
    Test that analyze_tone raises a ToneValidationError when analyzing an empty text.
    """
    with pytest.raises(ToneValidationError) as exc_info:
        analyze_tone("")
    
    assert str(exc_info.value) == "The input value must be a non-empty string."


def test_analyze_tone_low_confidence():
    """
    Test that analyze_tone correctly handles low-confidence results.
    """
    with requests_mock.Mocker() as mock:
        mock.post(INFERENCE_SERVICE_URL, json={
            "emotions": [
                {"emotion": "sadness", "percentage": 40.0},
                {"emotion": "neutral", "percentage": 60.0}
            ],
            "predominant_emotion": "neutral",
            "confidence": 40.0
        }, status_code=200)

        result = analyze_tone("I am not feeling great.")

        assert "emotions" in result
        assert result["predominant_emotion"] == "neutral"
        assert result["confidence"] == 40.0
        assert result["message"] == "Low confidence in the predominant emotion."
