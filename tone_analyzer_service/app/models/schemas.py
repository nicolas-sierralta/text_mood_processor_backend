from pydantic import BaseModel, Field
from typing import List

class EmotionDetail(BaseModel):
    """
    Represents a detected emotion and its associated percentage.
    """
    emotion: str = Field(..., description="The name of the detected emotion.")
    percentage: float = Field(..., description="The percentage of the detected emotion.")

class ToneAnalysisRequest(BaseModel):
    """
    Schema for the request body to analyze the tone of the text.
    """
    text: str = Field(..., min_length=1, description="The text to be analyzed.")

class ToneAnalysisResponse(BaseModel):
    """
    Schema for the response body containing tone analysis results.
    """
    emotions: List[EmotionDetail] = Field(..., description="List of detected emotions with their percentages.")
    predominant_emotion: str = Field(..., description="The predominant emotion detected.")
    confidence: float = Field(..., description="Confidence score for the predominant emotion.")
