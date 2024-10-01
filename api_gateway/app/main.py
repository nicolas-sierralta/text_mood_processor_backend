from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes
from app.config.logger import get_logger
from app.services.tone_analyzer_service import tone_analyzer_service
from app.utils.exceptions import APIError

# Initialize logger
logger = get_logger("api_gateway")

# Define the lifespan function for application lifecycle management
async def lifespan(app: FastAPI):
    """
    Lifespan function for managing startup and shutdown processes of the FastAPI application.

    Yields control between startup and shutdown, ensuring proper resource management.
    """
    try:
        # Actions to perform during startup
        logger.info("Starting FastAPI application")
        yield  # This yields control, running the application between startup and shutdown
    
    except APIError as e:
        logger.error(f"API Error during startup: {e.detail}")
        raise e

    except Exception as e:
        logger.error(f"Unexpected error during startup: {e}")
        raise e

    finally:
        # Actions to perform during shutdown
        logger.info("Shutting down FastAPI application")
        try:
            await tone_analyzer_service.close()  # Gracefully close the HTTP client on shutdown
            logger.info("Tone Analyzer Service closed successfully")
        except Exception as e:
            logger.error(f"Error while shutting down Tone Analyzer Service: {e}")

# Create the FastAPI app instance with lifespan function
app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include the API routes
app.include_router(routes.router, prefix="/api")

# Health check endpoint
@app.get("/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify the API Gateway is running.
    """
    return {"status": "ok", "message": "API Gateway is up and running!"}
