import pytest
from app.utils.validators import validate_non_empty_string, validate_string_length
from app.utils.exceptions import InferenceValidationError

def test_validate_non_empty_string_error():
    """
    Test that the validate_non_empty_string function raises InferenceValidationError with expected detail.
    """
    with pytest.raises(InferenceValidationError) as exc_info:
        validate_non_empty_string("")
    assert str(exc_info.value) == "The value must be a non-empty string."
    assert exc_info.value.detail == "The value must be a non-empty string."

def test_validate_non_empty_string_success():
    """
    Test that the validate_non_empty_string function does not raise an error for valid input.
    """
    try:
        validate_non_empty_string("Valid input")
    except InferenceValidationError:
        pytest.fail("InferenceValidationError raised unexpectedly!")

def test_validate_string_length_error():
    """
    Test that the validate_string_length function raises InferenceValidationError when the string exceeds max length.
    """
    with pytest.raises(InferenceValidationError) as exc_info:
        validate_string_length("This string is too long", 10)
    assert str(exc_info.value).startswith("The string length should not exceed")
    assert "10 characters" in str(exc_info.value)
    assert exc_info.value.detail.startswith("The string length should not exceed")

def test_validate_string_length_success():
    """
    Test that the validate_string_length function does not raise an error for a valid string length.
    """
    try:
        validate_string_length("Short string", 50)
    except InferenceValidationError:
        pytest.fail("InferenceValidationError raised unexpectedly!")
