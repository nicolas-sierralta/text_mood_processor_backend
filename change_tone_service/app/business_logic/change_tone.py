from openai import OpenAI
from app.config.settings import change_tone_settings
from app.utils.exceptions import ChangeToneRuntimeError
from app.utils.validators import validate_non_empty_string
from app.config.logger import get_logger

# Initialize the logger
logger = get_logger(__name__)

# Create the OpenAI client with the provided API key
client = OpenAI(api_key=change_tone_settings.OPENAI_API_KEY)
model = change_tone_settings.OPENAI_MODEL

def change_tone(text: str, target_tone: str) -> dict:
    """
    Change the tone of the provided text using OpenAI's API.

    This function takes an input text and a target tone and modifies the text to match the 
    requested tone using OpenAI's language model. It ensures that the meaning and structure
    of the original text remain intact.

    Args:
        text (str): The original text to modify.
        target_tone (str): The target tone to apply to the text.

    Returns:
        dict: A dictionary containing the original text, the modified text, and the applied tone.

    Raises:
        ChangeToneRuntimeError: If the OpenAI API response is invalid or if any other error occurs.
    """
    # Validate the input text and target tone
    validate_non_empty_string(text)
    validate_non_empty_string(target_tone)

    try:
        logger.info(f"Changing tone of text: {text[:100]}... to tone: {target_tone}")

        # Create the prompt for OpenAI, specifying the required tone change
        prompt = (f"Change the tone of the following text to a {target_tone} tone. "
                  f"Do not add new content. Do not change the meaning or structure of the text. "
                  f"Keep the text as close to the original as possible.\n\n"
                  f"Text: {text}")

        # Use OpenAI client to send the request
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an assistant that modifies text tone."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=change_tone_settings.MAX_TOKENS,
            temperature=0,  # Set temperature to 0 for deterministic output
            n=1
        )

        # Extract the modified text from the API response
        modified_text = response.choices[0].message.content.strip()

        logger.info(f"Tone changed successfully for text: {text[:50]}...")
        return {
            "original_text": text,
            "modified_text": modified_text,
            "applied_tone": target_tone
        }

    except KeyError as e:
        # Handle error if the response structure is not as expected
        logger.error(f"Invalid response structure: {e}")
        raise ChangeToneRuntimeError("Failed to parse the response from OpenAI's API.")
    
    except Exception as e:
        # Handle any other unexpected errors
        logger.error(f"Error during tone change: {e}")
        raise ChangeToneRuntimeError(f"Tone change failed: {str(e)}")
