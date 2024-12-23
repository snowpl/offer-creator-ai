from app.domain.chat.chat_service import ChatService

# Service Provider
def get_chat_service() -> ChatService:
    # You can add logic here to manage service lifecycles or configurations
    return ChatService
