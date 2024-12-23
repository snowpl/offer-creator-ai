from fastapi import APIRouter
from api.v1.endpoints import router

# Create the main API router
api_router = APIRouter()

# Include the endpoints from different modules
api_router.include_router(router, prefix="/example", tags=["Example"])
