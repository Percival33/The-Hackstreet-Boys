import json
from typing import Tuple

from pydantic import BaseModel

from src.application.generation_settings import GptGenerationSettings
from src.domain.action import ActionName, ALL_ACTIONS
from src.domain.conversation import Conversation, Message
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.triage.prompts import triage_step, triage_step_system


class TriageModelResponse(BaseModel):
    available_actions: list[ActionName]
    available_choices: list[str]
    response: str


class Triage:
    def __init__(
            self,
            language: str
    ):
        self.gpt_client = GptClient()
        self.language = language

    def step(
            self,
            conversation: Conversation,
            depth: int = 0
    ) -> TriageModelResponse:
        self.gpt_client.creator.add_from_conversation(conversation.messages)
        if len(conversation.messages) > 1:
            current_actions = conversation.messages[-2].choices
        else:
            current_actions = ALL_ACTIONS.values()
        actions_str = self.__parse_actions(current_actions)

        generation_settings = GptGenerationSettings(
            response_format=TriageModelResponse
        )

        if len(conversation.messages) == 1:
            self.gpt_client.creator.add(
                system=triage_step_system(actions_str),
                assistant=triage_step(self.language)
            )
        self.gpt_client.creator.add(
            user=conversation.messages[-1].text,
        )
        response = self.gpt_client.response(
            messages=self.gpt_client.creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )
        self.gpt_client.creator.clear()
        response = json.loads(response)
        return TriageModelResponse(**response)



    # @staticmethod
    # def __parse_actions(actions: list[str] | None) -> str:
    #     if actions is None:
    #         return ''
    #     res = ''
    #     for i, action_choice in enumerate(actions):
    #         action = ALL_ACTIONS[action_choice.action_name]
    #         res += f'{i + 1}. {action.name.value}\n'
    #         res += f'{action.description}\n'
    #         res += f'-----------------------\n'
    #     return res

    def __rollback(self):
        pass
