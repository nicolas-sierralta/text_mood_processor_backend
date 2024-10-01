class InferenceServiceError(Exception):
    """
    Base class for all exceptions related to the Inference Service.
    """
    def __init__(self, detail: str, status_code: int = 500):
        """
        Initializes the InferenceServiceError with a detailed message and a status code.

        Args:
            detail (str): A message providing details about the exception.
            status_code (int): The HTTP status code associated with the error (default: 500).
        """
        self.detail = detail
        self.status_code = status_code
        super().__init__(detail)


class InferenceValidationError(InferenceServiceError):
    """
    Exception raised for validation errors in the inference process.
    """
    def __init__(self, detail: str = "Validation error occurred."):
        """
        Initializes the InferenceValidationError with a status code of 400.

        Args:
            detail (str): A message providing details about the validation error.
        """
        super().__init__(detail, status_code=400)


class ModelLoadingError(InferenceServiceError):
    """
    Exception raised when there is an error loading the model.
    """
    def __init__(self, detail: str = "Failed to load the model."):
        """
        Initializes the ModelLoadingError with a default message and a 500 status code.

        Args:
            detail (str): A message providing details about the model loading error.
        """
        super().__init__(detail)


class InferenceRuntimeError(InferenceServiceError):
    """
    Exception raised for unexpected errors during inference execution.
    """
    def __init__(self, detail: str = "An error occurred during inference execution."):
        """
        Initializes the InferenceRuntimeError with a default message and a 500 status code.

        Args:
            detail (str): A message providing details about the inference runtime error.
        """
        super().__init__(detail)
