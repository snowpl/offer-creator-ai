import json
from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import ChatService, get_chat_service

router = APIRouter()

@router.get("/", summary="Test")
async def get_example():
    """
    Test.
    """
    return {"message": "This is example data"}

@router.post("/generate-utterance", summary="Generates reply based on AI")
async def create_example(
    message: str,
    service: ChatService = Depends(get_chat_service())
    ):
    """
    Get reply from the LLM.
    """

    return await service.handle_chat_response(message)
