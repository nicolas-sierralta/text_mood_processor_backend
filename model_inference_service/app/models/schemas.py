from pydantic import BaseModel, Field, confloat
from typing import List

class InferenceRequest(BaseModel):
    """
    Schema for the request body that will perform the inference.
    
    This schema defines the structure of the input data required to perform
    an inference using the model. It expects the input text.
    """
    text: str = Field(
        ..., 
        min_length=1, 
        description="The text to be used for model inference."
    )  # The input text that will be analyzed by the model.

class EmotionDetail(BaseModel):
    """
    Represents a detected emotion and its percentage.
    
    This schema holds information about a single detected emotion, including its
    name and the percentage that indicates how strongly the emotion is represented.
    """
    emotion: str = Field(
        ..., 
        description="The name of the detected emotion."
    )  # The name of the emotion detected (e.g., 'joy', 'anger').

    percentage: confloat(ge=0, le=100) = Field(
        ..., 
        description="The percentage of the detected emotion."
    )  # The percentage indicating how much the emotion is represented in the text.

class InferenceResponse(BaseModel):
    """
    Schema for the response body that contains inference results.
    
    This schema defines the structure of the response after performing an inference
    on the input text. It includes a list of emotions with their percentages, the 
    predominant emotion, and the confidence level of that predominant emotion.
    """
    emotions: List[EmotionDetail] = Field(
        ..., 
        description="List of detected emotions with their percentages."
    )  # A list of emotions detected in the text with their respective percentages.

    predominant_emotion: str = Field(
        ..., 
        description="The predominant emotion detected in the text."
    )  # The emotion that was detected as the most dominant in the text.

    confidence: confloat(ge=0, le=100) = Field(
        ..., 
        description="The confidence percentage for the predominant emotion."
    )  # The confidence level (as a percentage) for the predominant emotion.
