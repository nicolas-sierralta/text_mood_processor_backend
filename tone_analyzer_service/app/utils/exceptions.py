class ToneAnalyzerError(Exception):
    """
    Base class for all exceptions related to the Tone Analyzer Service.
    """
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(detail)

class ToneValidationError(ToneAnalyzerError):
    """
    Raised for validation errors in the tone analyzer.
    """
    def __init__(self, detail: str):
        super().__init__(detail)

class ToneNotFoundError(ToneAnalyzerError):
    """
    Raised when a required tone or resource is not found.
    """
    def __init__(self, detail: str):
        super().__init__(detail)

class ToneProcessingError(ToneAnalyzerError):
    """
    Raised for processing errors in the tone analyzer.
    """
    def __init__(self, detail: str):
        super().__init__(detail)
