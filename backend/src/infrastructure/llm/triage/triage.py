from pydantic import BaseModel

from src.application.generation_settings import GptGenerationSettings
from src.domain.conversation import Conversation
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.triage.prompts import triage_step


class Action(BaseModel):
    name: str
    description: str
    tool: str


class TriageActionResponse(BaseModel):
    available_actions: list[Action]
    response: str
    rollback: bool


class Triage:
    def __init__(
            self,
            available_actions: list[Action],
            language: str
    ):
        self.available_actions = available_actions
        self.gpt_client = GptClient()
        self.actions_history: list[Action] = []
        self.language = language

    def step(
            self,
            conversation: Conversation,
            user_message: str,
            depth: int = 0
    ) -> str:
        current_actions = conversation.messages[-1].choices
        actions_str = self.parse_actions(current_actions)

        generation_settings = GptGenerationSettings(
            response_format=TriageActionResponse
        )
        self.gpt_client.creator.add(
            user='',
            assistant=triage_step(self.language),
            system=''
        )

        response = self.gpt_client.response(
            messages=self.gpt_client.creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )

        return ''

    @staticmethod
    def parse_actions(actions: list[Action]) -> str:
        res = ''
        for i, action in enumerate(actions):
            res += f'{i + 1}. {action.name}\n'
            res += f'{action.description}\n'
            res += f'-----------------------\n\n'
        return res

    def rollback(self):
        pass
