from lagom import Container, Singleton
from app.domain.chat.chat_service import ChatService
from app.domain.llms.gpt_client import GptClient
from lagom.integrations.fast_api import FastApiIntegration
from app.config import settings
from app.domain.llms.tokens import TokenWatcher
from app.domain.prompts.prompt_manager import PromptManager;

container = Container()

container[PromptManager] = PromptManager
container[TokenWatcher] = TokenWatcher
container[GptClient] = lambda c: GptClient(settings, token_watcher=c[TokenWatcher])
container[ChatService] = lambda c: ChatService(llm_client=c[GptClient], prompt_manager=c[PromptManager])

# Integrate Lagom with FastAPI
depts = FastApiIntegration(container)
