from fastapi import FastAPI
from app.config import settings
from app.presentation.fastapi_router import api_router

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="An API built with Domain-Driven Design principles",
    version=settings.API_VERSION,
)
# Include API routes
app.include_router(api_router)
