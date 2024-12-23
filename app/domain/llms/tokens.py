
from typing import Protocol

class TokenConsumption:
    def __init__(self, prompt_tokens: int, completition_tokens: int):
        self.prompt_tokens = prompt_tokens
        self.completition_tokens = completition_tokens

# class ITokenWatcher(Protocol):
#     def add_consumed_tokens(prompt_tokens: int, completition_tokens: int): ...
    
#     @property
#     def consumption(self) -> TokenConsumption:
#         pass

class TokenWatcher():
    def __init__(self, prompt_tokens: int, completition_tokens: int):
        self.prompt_tokens = 0
        self.completition_tokens = 0
        
    def add_consumed_tokens(self, prompt_tokens, completition_tokens):
        self.prompt_tokens += prompt_tokens
        self.completition_tokens += completition_tokens

    @property
    def consumption(self) -> TokenConsumption:
        return TokenConsumption(self.prompt_tokens, self.completition_tokens)