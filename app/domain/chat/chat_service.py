from typing import List, Optional, Dict, Any, Protocol
from fastapi import Depends
from app.domain.llms.gpt_client import ILlmClient
from app.domain.llms.tokens import ITokenWatcher, TokenConsumption
from app.domain.prompts.prompt_manager import PromptManager
from app.main import get_prompt_manager

class ConversationStatuses:
    Handover = "Handover"
    Finished = "Finished"

class HandleChatResponse:
    def __init__(self, content: str, conversation_status: str, token_consumption: TokenConsumption):
        self.content = content
        self.conversation_status = conversation_status
        self.token_consumption = token_consumption

class IChatService(Protocol):
    async def handle_chat_response(self, utterance: str) -> HandleChatResponse:
        pass

# class IIntentStrategy(Protocol):
#     @property
#     def intent_name(self) -> str:
#         pass

#     async def handle(self, utterance: str) -> str:
#         pass

class ChatService():
    def __init__(self, llm_client: ILlmClient, token_watcher: ITokenWatcher, prompt_manager: PromptManager = Depends(get_prompt_manager)):
        self = self
        self._llm_client = llm_client
        self.token_watcher = token_watcher
        self.prompt_manager = prompt_manager
        # self._strategies = strategies || , strategies: List[IIntentStrategy]

    async def handle_chat_response(self, utterance: str) -> HandleChatResponse:
        promptTemplate = self.prompt_manager.get_email_intent_classification_prompt()
        formatted_prompt = promptTemplate.format(USER_MESSAGE=utterance)
        return HandleChatResponse(
            "Hello from the service!",
            ConversationStatuses.Finished,
            TokenConsumption(100, 100)
        )
    
