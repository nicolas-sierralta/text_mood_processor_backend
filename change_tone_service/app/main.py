from fastapi import FastAPI, Request
from app.api.routes import router as change_tone_router  # Importa el router del change tone service
from app.config.logger import get_logger
from app.config.settings import change_tone_settings  # Importa la configuración del servicio
from contextlib import asynccontextmanager

# Initialize the logger for the Change Tone Service
logger = get_logger(__name__)

# Create an async context manager for the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Code to run on startup
        logger.info("Starting up the Change Tone Service...")
        
        yield  # Control passes to the application here
        
    except Exception as e:
        logger.error(f"Error during application lifespan: {e}")
        raise
    finally:
        # Code to run on shutdown
        logger.info("Shutting down the Change Tone Service...")

# Create an instance of the FastAPI application with lifespan
app = FastAPI(
    title=change_tone_settings.APP_NAME,
    debug=change_tone_settings.DEBUG,
    version="1.0.0",
    description="A service to change the tone of text using OpenAI.",
    lifespan=lifespan
)

# Include the API router from the routes module
app.include_router(change_tone_router, prefix="/api", tags=["Change Tone"])

# Health check endpoint
@app.get("/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify the Change Tone Service is running.
    """
    return {"status": "ok", "message": "Change Tone Service is up and running!"}
