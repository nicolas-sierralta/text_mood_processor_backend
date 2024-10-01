class ChangeToneServiceError(Exception):
    """
    Base class for all exceptions related to the Change Tone Service.
    """
    def __init__(self, detail: str, status_code: int = 500):
        """
        Initializes the ChangeToneServiceError with a detailed message and a status code.

        Args:
            detail (str): A message providing details about the exception.
            status_code (int): The HTTP status code associated with the error (default: 500).
        """
        self.detail = detail
        self.status_code = status_code
        super().__init__(detail)


class ChangeToneValidationError(ChangeToneServiceError):
    """
    Exception raised for validation errors in the change tone process.
    """
    def __init__(self, detail: str = "Validation error occurred while changing tone."):
        """
        Initializes the ChangeToneValidationError with a status code of 400.

        Args:
            detail (str): A message providing details about the validation error.
        """
        super().__init__(detail, status_code=400)


class ChangeToneRuntimeError(ChangeToneServiceError):
    """
    Exception raised for unexpected errors during tone change execution.
    """
    def __init__(self, detail: str = "An error occurred during tone change execution."):
        """
        Initializes the ChangeToneRuntimeError with a default message and a 500 status code.

        Args:
            detail (str): A message providing details about the tone change runtime error.
        """
        super().__init__(detail)

