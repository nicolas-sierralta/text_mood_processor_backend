import pytest
from app.utils.exceptions import InferenceValidationError, ModelLoadingError, InferenceRuntimeError

def test_inference_validation_error():
    """
    Test that the InferenceValidationError is raised with the expected detail message.
    """
    with pytest.raises(InferenceValidationError) as exc_info:
        raise InferenceValidationError("Validation failed")
    assert str(exc_info.value) == "Validation failed"
    assert exc_info.value.detail == "Validation failed"
    assert exc_info.value.status_code == 400


def test_model_loading_error():
    """
    Test that the ModelLoadingError is raised with the expected detail message.
    """
    with pytest.raises(ModelLoadingError) as exc_info:
        raise ModelLoadingError("Model not found")
    assert str(exc_info.value) == "Model not found"
    assert exc_info.value.detail == "Model not found"
    assert exc_info.value.status_code == 500


def test_inference_runtime_error():
    """
    Test that the InferenceRuntimeError is raised with the expected detail message.
    """
    with pytest.raises(InferenceRuntimeError) as exc_info:
        raise InferenceRuntimeError("Inference failed")
