from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import ChatService, get_chat_service
from app.domain.chat.chat_service import HandleChatResponse

router = APIRouter()

@router.post("/generate-utterance", summary="Generates reply based on AI", response_model=None)
async def create_example(
    message: str,
    service: ChatService = Depends(get_chat_service)
    ) -> HandleChatResponse:
    """
    Get reply from the LLM.
    """
    print(message)
    response = await service.handle_chat_response(utterance=message)
    return {"response": response}
