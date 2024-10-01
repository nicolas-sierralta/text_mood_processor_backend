from fastapi import FastAPI, Request
from app.api.routes import router as inference_router
from app.config.logger import get_logger
from app.config.settings import settings
from contextlib import asynccontextmanager

# Initialize the logger for the Model Inference Service
logger = get_logger(__name__)

# Create an async context manager for the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Code to run on startup
        logger.info("Starting up the Model Inference Service...")
        
        yield  # Control passes to the application here
        
    except Exception as e:
        logger.error(f"Error during application lifespan: {e}")
        raise
    finally:
        # Code to run on shutdown
        logger.info("Shutting down the Model Inference Service...")

# Create an instance of the FastAPI application with lifespan
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    description="A service to perform model inference.",
    lifespan=lifespan
)

# Include the API router from the routes module
app.include_router(inference_router, prefix="/api", tags=["Inference"])

# Health check endpoint
@app.get("/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify the Model Inference Service is running.
    """
    return {"status": "ok", "message": "Model Inference Service is up and running!"}

