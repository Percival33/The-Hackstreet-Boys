from src.infrastructure.llm.gpt_client import GptClient


class Triage:
    def __init__(
            self,
            available_actions: list[str]
    ):
        self.available_actions = available_actions
        self.client = GptClient()

    def start_conversation(self):
        pass
