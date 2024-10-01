import pytest
from app.utils.exceptions import ToneValidationError, ToneNotFoundError, ToneProcessingError

def test_tone_validation_error():
    """
    Test that ToneValidationError is raised correctly with the expected detail message.
    """
    with pytest.raises(ToneValidationError) as exc_info:
        raise ToneValidationError("Validation failed")
    assert str(exc_info.value) == "Validation failed"
    assert exc_info.value.detail == "Validation failed"  # Verifies the `detail` attribute

def test_tone_not_found_error():
    """
    Test that ToneNotFoundError is raised correctly with the expected detail message.
    """
    with pytest.raises(ToneNotFoundError) as exc_info:
        raise ToneNotFoundError("Tone not found")
    assert str(exc_info.value) == "Tone not found"
    assert exc_info.value.detail == "Tone not found"  # Verifies the `detail` attribute

def test_tone_processing_error():
    """
    Test that ToneProcessingError is raised correctly with the expected detail message.
    """
    with pytest.raises(ToneProcessingError) as exc_info:
        raise ToneProcessingError("Processing error")
    assert str(exc_info.value) == "Processing error"
    assert exc_info.value.detail == "Processing error"  # Verifies the `detail` attribute
