import pytest
from app.utils.exceptions import ValidationError, NotFoundError, ConflictError

def test_validation_error():
    """
    Test that the ValidationError is raised with the expected detail message.
    """
    with pytest.raises(ValidationError) as exc_info:
        raise ValidationError("Validation failed")
    assert str(exc_info.value) == "Validation failed"
    assert exc_info.value.detail == "Validation failed"

def test_not_found_error():
    """
    Test that the NotFoundError is raised with the expected detail message.
    """
    with pytest.raises(NotFoundError) as exc_info:
        raise NotFoundError("Resource not found")
    assert str(exc_info.value) == "Resource not found"
    assert exc_info.value.detail == "Resource not found"

def test_conflict_error():
    """
    Test that the ConflictError is raised with the expected detail message.
    """
    with pytest.raises(ConflictError) as exc_info:
        raise ConflictError("Conflict occurred")
    assert str(exc_info.value) == "Conflict occurred"
    assert exc_info.value.detail == "Conflict occurred"
