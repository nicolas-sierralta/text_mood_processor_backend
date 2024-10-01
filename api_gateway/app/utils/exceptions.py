class APIError(Exception):
    """
    Base class for all exceptions related to the API.

    Attributes:
        detail (str): A message providing details about the exception.
    """
    def __init__(self, detail: str):
        """
        Initializes the APIError with a detailed message.

        Args:
            detail (str): A message providing details about the exception.
        """
        self.detail = detail
        super().__init__(detail)


class ValidationError(APIError):
    """
    Exception raised for validation errors (e.g., invalid input data).

    Attributes:
        detail (str): A message providing details about the validation error.
    """
    def __init__(self, detail: str = "Validation error occurred."):
        """
        Initializes the ValidationError with a detailed message.

        Args:
            detail (str): A message providing details about the validation error.
        """
        super().__init__(detail)


class NotFoundError(APIError):
    """
    Exception raised when a requested resource is not found.

    Attributes:
        detail (str): A message indicating the resource was not found.
    """
    def __init__(self, detail: str = "The requested resource was not found."):
        """
        Initializes the NotFoundError with a detailed message.

        Args:
            detail (str): A message providing details about the missing resource.
        """
        super().__init__(detail)


class ConflictError(APIError):
    """
    Exception raised for conflicts (e.g., attempting to create a duplicate resource).

    Attributes:
        detail (str): A message indicating the nature of the conflict.
    """
    def __init__(self, detail: str = "A conflict occurred."):
        """
        Initializes the ConflictError with a detailed message.

        Args:
            detail (str): A message providing details about the conflict.
        """
        super().__init__(detail)
