from pydantic import BaseModel, Field

class ChangeToneRequest(BaseModel):
    """
    Schema for the request body that will perform the tone change.
    
    This schema defines the structure of the input data for the tone change request.
    It expects two fields: the original text to modify and the target tone to apply.
    """
    text: str = Field(
        ..., 
        min_length=1, 
        description="The text to be modified."
    )  # The text that will be changed based on the target tone.
    
    target_tone: str = Field(
        ..., 
        description="The tone to change the text to (e.g., 'friendly', 'serious')."
    )  # The tone that should be applied to the text.

class ChangeToneResponse(BaseModel):
    """
    Schema for the response body that contains the modified text.
    
    This schema defines the structure of the response returned after the tone change.
    It includes the original text, the modified text, and the applied tone.
    """
    original_text: str = Field(
        ..., 
        description="The original text before the tone change."
    )  # The original text provided in the request.
    
    modified_text: str = Field(
        ..., 
        description="The text after the tone change."
    )  # The modified text returned after applying the target tone.
    
    applied_tone: str = Field(
        ..., 
        description="The tone that was applied to the modified text."
    )  # The tone that was successfully applied to the original text.
