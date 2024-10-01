import pytest
from app.utils.validators import validate_non_empty_string, validate_string_length
from app.utils.exceptions import ToneValidationError

def test_validate_non_empty_string_valid():
    # Test with a valid non-empty string
    validate_non_empty_string("Valid string")

def test_validate_non_empty_string_empty():
    # Test with an empty string (should raise ToneValidationError)
    with pytest.raises(ToneValidationError):
        validate_non_empty_string("")

def test_validate_non_empty_string_whitespace():
    # Test with a string that contains only whitespace (should raise ToneValidationError)
    with pytest.raises(ToneValidationError):
        validate_non_empty_string("   ")

def test_validate_string_length_valid():
    # Test with a string that does not exceed the maximum length
    validate_string_length("Valid string", max_length=20)

def test_validate_string_length_exceeds_max():
    # Test with a string that exceeds the maximum length (should raise ToneValidationError)
    with pytest.raises(ToneValidationError):
        validate_string_length("This is a very long text exceeding the limit", max_length=10)
