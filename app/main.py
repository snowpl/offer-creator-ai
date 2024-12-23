from fastapi import FastAPI
from lagom.integrations.fast_api import FastApiIntegration
from app.config import settings
from app.presentation.fastapi_router import api_router
from app.dependencies import container

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="An API built with Domain-Driven Design principles",
    version=settings.API_VERSION,
)

# Include API routes
app.include_router(api_router)

# Integrate Lagom with FastAPI
lagom = FastApiIntegration(container)

# For running locally, uncomment below:
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
