from fastapi import FastAPI
from core.config import settings
from presentation.fastapi_router import api_router
from app.domain.prompts.prompt_manager import PromptManager

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="An API built with Domain-Driven Design principles",
    version=settings.API_VERSION,
)
prompt_manager = PromptManager()

def get_prompt_manager() -> PromptManager:
    return prompt_manager

# Include API routes
app.include_router(api_router)

# Middleware, event handlers, or any other app configuration can go here

@app.on_event("startup")
async def startup_event():
    """
    Actions to perform when the application starts.
    For example, database connections or preloading data.
    """
    print("Application startup logic here.")

@app.on_event("shutdown")
async def shutdown_event():
    """
    Actions to perform when the application is shutting down.
    For example, cleaning up resources or closing connections.
    """
    print("Application shutdown logic here.")

# For running locally, uncomment below:
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
