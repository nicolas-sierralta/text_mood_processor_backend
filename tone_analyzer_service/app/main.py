from fastapi import FastAPI
from app.api.routes import router as tone_analyzer_router
from app.config.settings import settings
from app.config.logger import get_logger
from contextlib import asynccontextmanager

# Initialize logger instance
logger = get_logger("tone_analyzer_service")

# Async context manager for application lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up the Tone Analyzer Service...")
    yield
    logger.info("Shutting down the Tone Analyzer Service...")

# Create FastAPI app with lifespan
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    description="A service to analyze the tone of text.",
    lifespan=lifespan
)

# Register the API routes
app.include_router(tone_analyzer_router, prefix="/api", tags=["Tone Analysis"])

# Health check endpoint
@app.get("/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify the Tone Analyzer Service is running.
    """
    return {"status": "ok", "message": "Tone Analyzer Service is up and running!"}
