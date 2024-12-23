from pydantic import BaseModel

class TokenConsumption(BaseModel):
    prompt_tokens: int
    completition_tokens: int

class TokenWatcher():
    def __init__(self):
        self.prompt_tokens = 0
        self.completition_tokens = 0
        
    def add_consumed_tokens(self, prompt_tokens, completition_tokens):
        self.prompt_tokens += prompt_tokens
        self.completition_tokens += completition_tokens

    @property
    def consumption(self) -> TokenConsumption:
        return TokenConsumption(
            prompt_tokens=self.prompt_tokens,
             completition_tokens= self.completition_tokens
        )