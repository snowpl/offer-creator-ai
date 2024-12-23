import json
from langchain.prompts import PromptTemplate

#This is for local-only in a real-world system it would be best to adust this to a redis-based
class PromptManager:
    _instance =None #Singleton instance
    prompts = {}

    def __new__(self):
        if self._instance is None:
            self._instance = super(PromptManager, self).__new__(self)
            self._instance._load_prompts()
        return self._instance
    
    def _load_prompts(self):
        try:
            with open("prompts.json", "r") as file:
                self.prompts = json.load(file)["prompts"]
        except FileNotFoundError:
            raise RuntimeError("Prompts files not found. Please make sure the file exists.")
    
    def _get_prompt(self, prompt_name, version=None):
        if prompt_name not in self.prompts:
            raise ValueError("Prompt '{prompt_name}' not found.")
        
        prompt_data = self.prompts[prompt_name]
        if version is None:
            version = prompt_data["current_version"]

        if version not in prompt_data["versions"]:
            raise ValueError(f"Version '{version}' not available for prompt '{prompt_name}'.")

        return prompt_data["versions"][version]
    
    def get_email_intent_classification_prompt(self) -> PromptTemplate:
        prompt = self._get_prompt("email_intent_classification")
        return PromptTemplate(
            input_variables=prompt["input_variables"],
            template=prompt["template"]
        )
