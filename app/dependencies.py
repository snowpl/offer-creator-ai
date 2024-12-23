from lagom import Container, Singleton
from app.domain.chat.chat_service import ChatService
from app.domain.llms.gpt_client import GptClient
from app.config import settings
from app.domain.llms.tokens import ITokenWatcher, TokenWatcher
from app.domain.prompts.prompt_manager import PromptManager;

container = Container()

container[PromptManager] = Singleton(PromptManager)
container[ITokenWatcher] = TokenWatcher
container[GptClient] = lambda c: GptClient(settings, token_watcher=c[ITokenWatcher])
container[ChatService] = lambda c: ChatService(llm_client=c[GptClient], prompt_manager=c[PromptManager])
