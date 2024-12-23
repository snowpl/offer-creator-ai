from fastapi import APIRouter
from app.domain.chat.chat_service import HandleChatResponse, ChatService
from app.dependencies import depts

router = APIRouter()

@router.post("/generate-utterance", summary="Generates reply based on AI", response_model=None)
async def create_example(
    message: str,
    service: ChatService = depts.depends(ChatService)
    ) -> HandleChatResponse:
    """
    Get reply from the LLM.
    """
    print(message)
    response = await service.handle_chat_response(utterance=message)
    return response
