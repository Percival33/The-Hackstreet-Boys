from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.gpt_prompt_creator import GptPromptCreator


class PromptVerifier:
    def __init__(self):
        pass

    @classmethod
    def verify(cls, prompt: str) -> bool:
        creator = GptPromptCreator()
        client = GptClient()

        creator.add(
            # assistant=
            user=prompt
        )
