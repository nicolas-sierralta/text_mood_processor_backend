import pytest
from app.utils.exceptions import ChangeToneServiceError, ChangeToneValidationError, ChangeToneRuntimeError

def test_change_tone_service_error():
    error_message = "This is a general error."
    exception = ChangeToneServiceError(error_message)
    
    assert exception.detail == error_message
    assert exception.status_code == 500  # Default status code

def test_change_tone_validation_error():
    error_message = "Invalid tone provided."
    exception = ChangeToneValidationError(error_message)
    
    assert exception.detail == error_message
    assert exception.status_code == 400  # Validation errors should have a 400 status code

    # Test with default message
    default_exception = ChangeToneValidationError()
    assert default_exception.detail == "Validation error occurred while changing tone."
    assert default_exception.status_code == 400

def test_change_tone_runtime_error():
    error_message = "Unexpected error during tone change."
    exception = ChangeToneRuntimeError(error_message)
    
    assert exception.detail == error_message
    assert exception.status_code == 500  # Runtime errors should have a 500 status code

    # Test with default message
    default_exception = ChangeToneRuntimeError()
    assert default_exception.detail == "An error occurred during tone change execution."
    assert default_exception.status_code == 500
