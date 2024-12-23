import json
import os
from langchain.prompts import PromptTemplate

#This is for local-only in a real-world system it would be best to adust this to a redis-based
class PromptManager:
    prompts = {}
    def __init__(self):
        self._load_prompts()
        pass
    
    def _load_prompts(self):
        try:
            base_dir = os.path.dirname(__file__)  # Directory of the current script
            file_path = os.path.join(base_dir, "prompts.json")
            with open(file_path, "r") as file:
                self.prompts = json.load(file)["prompts"]
        except FileNotFoundError:
            raise RuntimeError("Prompts files not found. Please make sure the file exists.")
    
    def _get_prompt(self, prompt_name, version=None):
        print(self.prompts)
        if prompt_name not in self.prompts:
            raise ValueError("Prompt '{prompt_name}' not found.")
        
        prompt_data = self.prompts[prompt_name]
        if version is None:
            version = prompt_data["current_version"]

        if version not in prompt_data["versions"]:
            raise ValueError(f"Version '{version}' not available for prompt '{prompt_name}'.")

        return prompt_data["versions"][version]
    
    def get_email_intent_classification_prompt(self) -> PromptTemplate:
        print('hello from Prompt Manager')
        prompt = self._get_prompt("email_intent_classification")
        return PromptTemplate(
            input_variables=prompt["input_variables"],
            template=prompt["template"]
        )
    
    def get_no_detected_intent_prompt(self) -> PromptTemplate:
        prompt = self._get_prompt("no_detected_intent")
        return PromptTemplate(
            template=prompt["template"],
            input_variables=prompt["input_variables"]
        )
