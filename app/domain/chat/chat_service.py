import re
from typing import List, Optional, Dict, Any, Protocol
from fastapi import Depends
from app.utils import get_gpt_client
from app.domain.llms.gpt_client import GptClient, ILlmClient
from app.domain.llms.tokens import TokenConsumption, TokenWatcher
from app.domain.prompts.prompt_manager import PromptManager

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
    def __init__(self, llm_client: GptClient = Depends(get_gpt_client), prompt_manager: PromptManager = None):
        self = self
        if prompt_manager is None:
            from app.main import get_prompt_manager
            self.prompt_manager = get_prompt_manager()
        if llm_client is None:
            self._llm_client = llm_client
        #self.token_watcher = token_watcher
        # self._strategies = strategies || , strategies: List[IIntentStrategy]

    async def handle_chat_response(self, utterance: str) -> HandleChatResponse:
        print('hello')
        intents = await self.handle_intent(utterance)
        print(intents)
        return HandleChatResponse(
            "123",
            ConversationStatuses.Finished,
            TokenConsumption(100, 100)
        )
    
    async def handle_intent(self, utterance) -> List[str]:
        promptTemplate = self.prompt_manager.get_email_intent_classification_prompt()
        formatted_prompt = promptTemplate.format(USER_MESSAGE=utterance)
        print(formatted_prompt)
        intents_array = await self._llm_client.generate_message_async(formatted_prompt, "text")
        return re.sub(r"\s+", "", intents_array).split(',')
    
    async def get_no_detected_intent_message(self) -> str:
        promptTemplate = self.prompt_manager.get_no_detected_intent_prompt()
        return await self._llm_client.generate_message_async(promptTemplate.format(), "text")
    
