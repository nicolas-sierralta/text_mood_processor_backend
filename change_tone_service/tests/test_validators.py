import pytest
from app.utils.validators import validate_non_empty_string, validate_string_length
from app.utils.exceptions import ChangeToneValidationError

def test_validate_non_empty_string():
    # Test with a valid non-empty string
    try:
        validate_non_empty_string("Hello")
    except ChangeToneValidationError:
        pytest.fail("Unexpected ChangeToneValidationError raised.")

    # Test with an empty string
    with pytest.raises(ChangeToneValidationError) as excinfo:
        validate_non_empty_string("")
    assert str(excinfo.value) == "The value must be a non-empty string."

    # Test with a string containing only whitespace
    with pytest.raises(ChangeToneValidationError) as excinfo:
        validate_non_empty_string("   ")
    assert str(excinfo.value) == "The value must be a non-empty string."

    # Test with a non-string value
    with pytest.raises(ChangeToneValidationError) as excinfo:
        validate_non_empty_string(123)
    assert str(excinfo.value) == "Expected type 'str' but got 'int'"

def test_validate_string_length():
    max_length = 10

    # Test with a valid string length
    try:
        validate_string_length("Hello", max_length)
    except ChangeToneValidationError:
        pytest.fail("Unexpected ChangeToneValidationError raised.")

    # Test with a string exceeding the maximum length
    with pytest.raises(ChangeToneValidationError) as excinfo:
        validate_string_length("Hello, World!", max_length)
    assert str(excinfo.value) == f"The string length should not exceed {max_length} characters. Given length: {len('Hello, World!')}"

    # Test with a non-string value
    with pytest.raises(ChangeToneValidationError) as excinfo:
        validate_string_length(12345, max_length)
    assert str(excinfo.value) == "Expected type 'str' but got 'int'"
