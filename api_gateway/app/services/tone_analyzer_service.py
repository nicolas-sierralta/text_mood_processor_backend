import logging
from httpx import AsyncClient, HTTPStatusError
from fastapi import HTTPException
from app.config.settings import settings

# Initialize logger for the ToneAnalyzerService
logger = logging.getLogger("api_gateway")

class ToneAnalyzerService:
    """
    Service to interact with the Tone Analyzer microservice via asynchronous HTTP requests.
    """

    def __init__(self):
        """
        Initializes the ToneAnalyzerService with an asynchronous HTTP client.
        """
        self.client = AsyncClient()  # Persistent HTTP client across requests
        self.url = settings.TONE_ANALYZER_URL

    async def analyze_tone(self, text: str) -> dict:
        """
        Sends text to the Tone Analyzer Service and retrieves the tone analysis.

        Args:
            text (str): The input text to analyze.

        Returns:
            dict: Response containing the tone analysis results.

        Raises:
            HTTPException: If a non-200 response is received from the service or any error occurs.
        """
        try:
            logger.info(f"Sending request to Tone Analyzer Service at {self.url}")
            
            # Make the asynchronous POST request to the Tone Analyzer Service
            response = await self.client.post(self.url, json={"text": text})

            # Handle non-200 responses
            if response.status_code != 200:
                logger.error(f"Tone Analyzer Service error: {response.status_code} - {response.text}")
                raise HTTPException(status_code=response.status_code, detail=response.json())

            # Log and return the successful response
            logger.info(f"Tone Analyzer Service response: {response.json()}")
            return response.json()

        except HTTPStatusError as http_exc:
            # Handle HTTP-related exceptions from httpx
            logger.error(f"HTTPStatusError: {http_exc.response.status_code} - {http_exc.response.text}")
            raise HTTPException(status_code=http_exc.response.status_code, detail=http_exc.response.json())

        except Exception as e:
            # Catch any unexpected exceptions and raise an internal server error
            logger.error(f"Unexpected error calling Tone Analyzer Service: {e}")
            raise HTTPException(status_code=500, detail="Internal error in Tone Analyzer Service")

    async def close(self):
        """
        Closes the asynchronous HTTP client, typically during application shutdown.
        """
        await self.client.aclose()

# Create an instance of ToneAnalyzerService
tone_analyzer_service = ToneAnalyzerService()