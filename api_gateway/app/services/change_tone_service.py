import logging
from httpx import AsyncClient, HTTPStatusError
from fastapi import HTTPException
from app.config.settings import settings

# Initialize logger for the ChangeToneService
logger = logging.getLogger("api_gateway")

class ChangeToneService:
    """
    Service to interact with the Change Tone microservice via asynchronous HTTP requests.
    """

    def __init__(self):
        """
        Initializes the ChangeToneService with an asynchronous HTTP client.
        """
        self.client = AsyncClient()  # Persistent HTTP client across requests
        self.url = settings.CHANGE_TONE_URL  # URL of the Change Tone microservice

    async def change_tone(self, text: str, target_tone: str) -> dict:
        """
        Sends text and target tone to the Change Tone Service and retrieves the modified text.

        Args:
            text (str): The input text to modify.
            target_tone (str): The target tone to apply to the text.

        Returns:
            dict: Response containing the modified text and applied tone.

        Raises:
            HTTPException: If a non-200 response is received from the service or any error occurs.
        """
        try:
            logger.info(f"Sending request to Change Tone Service at {self.url}")
            
            # Make the asynchronous POST request to the Change Tone Service
            response = await self.client.post(self.url, json={"text": text, "target_tone": target_tone})

            # Handle non-200 responses
            if response.status_code != 200:
                logger.error(f"Change Tone Service error: {response.status_code} - {response.text}")
                raise HTTPException(status_code=response.status_code, detail=response.json())

            # Log and return the successful response
            logger.info(f"Change Tone Service response: {response.json()}")
            return response.json()

        except HTTPStatusError as http_exc:
            # Handle HTTP-related exceptions from httpx
            logger.error(f"HTTPStatusError: {http_exc.response.status_code} - {http_exc.response.text}")
            raise HTTPException(status_code=http_exc.response.status_code, detail=http_exc.response.json())

        except Exception as e:
            # Catch any unexpected exceptions and raise an internal server error
            logger.error(f"Unexpected error calling Change Tone Service: {e}")
            raise HTTPException(status_code=500, detail="Internal error in Change Tone Service")

    async def close(self):
        """
        Closes the asynchronous HTTP client, typically during application shutdown.
        """
        await self.client.aclose()

# Create an instance of ChangeToneService
change_tone_service = ChangeToneService()
