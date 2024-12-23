
import json
from fastapi import Depends
import requests
from typing import Dict, Protocol
from app.domain.llms.tokens import ITokenWatcher, TokenWatcher

class ILlmClient(Protocol):
    async def generate_message_async(self, prompt: str, response_type: str):
        pass

class GptClient(ILlmClient):
    def __init__(self, llm_settings: Dict, token_watcher: ITokenWatcher = Depends(TokenWatcher)):
        self.llm_settings = llm_settings
        self.token_watcher = token_watcher

    async def generate_message_async(self, prompt: str, response_type: str = "json_object"):
        request_body = {
            "model": self.llm_settings["model_name"],
            "messages": [
                {
                    "role": "assistant",
                    "content": prompt
                }
            ],
            "max_tokens": self.llm_settings["max_tokens"],
            "temperature": self.llm_settings["temperature"],
            "response_format": {
                "type": response_type
            }
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(
                url = f"{self.base_url}/chat/completions",
                headers= headers,
                data=json.dumps(request_body)
            )

            if not response.ok:
                response.raise_for_status()
            
            body = await response.json()
            self.token_watcher.add_consumed_tokens(
                int(body["usage"]["prompt_tokens"]),
                int(body["usage"]["completion_tokens"])
            )
            return body["choices"][0]["message"]["content"]
        
        except requests.RequestException as e:
            self.logger.error(f"HTTP request failed: {str(e)}")
            raise