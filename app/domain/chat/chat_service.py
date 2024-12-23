import re
from typing import List, Optional, Dict, Any, Protocol
from fastapi import Depends
from pydantic import BaseModel
from app.domain.llms.gpt_client import GptClient, ILlmClient
from app.domain.llms.tokens import TokenConsumption, TokenWatcher
from app.domain.prompts.prompt_manager import PromptManager

class ConversationStatuses:
    Handover = "Handover"
    Finished = "Finished"

class HandleChatResponse(BaseModel):
        content: str
        conversation_status: str
        token_consumption: TokenConsumption

# class IIntentStrategy(Protocol):
#     @property
#     def intent_name(self) -> str:
#         pass

#     async def handle(self, utterance: str) -> str:
#         pass

class ChatService():
    def __init__(self, llm_client: GptClient = Depends(GptClient), prompt_manager: PromptManager = Depends(PromptManager)):
        self = self
        self.llm_client = llm_client
        self.prompt_manager = prompt_manager
        print(self.prompt_manager)
        #self.token_watcher = token_watcher
        # self._strategies = strategies || , strategies: List[IIntentStrategy]

    async def handle_chat_response(self, utterance: str) -> HandleChatResponse:
        print('hello')
        intents = await self.handle_intent(utterance)
        print(intents)
        return HandleChatResponse(
            content = "123",
            conversation_status = ConversationStatuses.Finished,
            token_consumption = TokenConsumption(prompt_tokens=100, completition_tokens=100)
        )
    
    async def handle_intent(self, utterance) -> List[str]:
        print(self.prompt_manager)
        promptTemplate = self.prompt_manager.get_email_intent_classification_prompt()
        print('got template')
        formatted_prompt = promptTemplate.format(USER_MESSAGE=utterance)
        print(formatted_prompt)
        intents_array = await self._llm_client.generate_message_async(formatted_prompt, "text")
        return re.sub(r"\s+", "", intents_array).split(',')
    
    async def get_no_detected_intent_message(self) -> str:
        promptTemplate = self.prompt_manager.get_no_detected_intent_prompt()
        return await self._llm_client.generate_message_async(promptTemplate.format(), "text")
    
