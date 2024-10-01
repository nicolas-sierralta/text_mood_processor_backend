from app.utils.exceptions import ToneValidationError

def validate_non_empty_string(value: str) -> None:
    """
    Validates that the input string is non-empty.
    """
    if not isinstance(value, str) or not value.strip():
        raise ToneValidationError("The input value must be a non-empty string.")

def validate_string_length(value: str, max_length: int) -> None:
    """
    Validates that the input string does not exceed the maximum length.
    """
    if len(value) > max_length:
        raise ToneValidationError(f"The string length should not exceed {max_length} characters. Given length: {len(value)}")
