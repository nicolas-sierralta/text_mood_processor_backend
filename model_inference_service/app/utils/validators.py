from typing import List, Dict
from app.utils.exceptions import InferenceValidationError

def validate_non_empty_string(value: str) -> None:
    """
    Validates that the input is a non-empty string.

    Args:
        value (str): The string value to validate.

    Raises:
        InferenceValidationError: If the input is not a valid non-empty string.
    """
    if not isinstance(value, str):
        raise InferenceValidationError(f"Expected type 'str' but got '{type(value).__name__}'")
    if not value.strip():
        raise InferenceValidationError("The value must be a non-empty string.")

def validate_string_length(value: str, max_length: int) -> None:
    """
    Validates that the input string does not exceed the maximum length.

    Args:
        value (str): The string value to validate.
        max_length (int): The maximum allowed length for the string.

    Raises:
        InferenceValidationError: If the input string exceeds the maximum length.
    """
    if not isinstance(value, str):
        raise InferenceValidationError(f"Expected type 'str' but got '{type(value).__name__}'")
    if len(value) > max_length:
        raise InferenceValidationError(f"The string length should not exceed {max_length} characters. "
                                       f"Given length: {len(value)}")
