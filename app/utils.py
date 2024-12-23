from app.domain.llms.gpt_client import GptClient
from app.domain.llms.tokens import TokenWatcher

def get_gpt_client() -> GptClient:
    llm_settings = {
        "model_name": "gpt-4",
        "max_tokens": 1000,
        "temperature": 0.7,
    }
    token_watcher = TokenWatcher()  # Replace with your actual implementation
    return GptClient(llm_settings, token_watcher)
