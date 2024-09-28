import json
from typing import List

from pydantic import BaseModel
from src.application.generation_settings import GptGenerationSettings
from src.domain.action import ActionName, ALL_ACTIONS, Action
from src.domain.conversation import Conversation, Message
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.gpt_prompt_creator import GptPromptCreator
from src.infrastructure.llm.triage.prompts import triage_step_action, triage_step_response_system, triage_step_response, \
    triage_step_action_system


class TriageStepResponse(BaseModel):
    available_actions: list[ActionName]
    available_choices: list[str]
    response: str


class TriageModelActions(BaseModel):
    actions_to_remove: list[ActionName]


class TriageModelResponse(BaseModel):
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
    ) -> TriageStepResponse:
        self.gpt_client.creator.add_from_conversation(conversation.messages)
        current_actions = conversation.available_actions
        actions_str = self.__parse_actions(current_actions)

        initial_messages = self.gpt_client.creator.messages

        def filter_actions(actions: list[Action]) -> list[Action]:
            creator = GptPromptCreator()
            creator.add_prebuilt(initial_messages)
            generation_settings = GptGenerationSettings(
                response_format=TriageModelActions
            )
            creator.add(
                system=triage_step_action_system(actions_str),
                assistant=triage_step_action()
            )
            response = self.gpt_client.response(
                messages=creator.messages,
                generation_settings=generation_settings,
                preset=[]
            )

            creator.clear()

            actions_to_remove = TriageModelActions(**json.loads(response)).actions_to_remove
            actions_to_keep = [action for action in actions if action.name not in actions_to_remove]
            return actions_to_keep

        def conversation_response() -> TriageStepResponse:
            creator = GptPromptCreator()
            creator.add_prebuilt(initial_messages)
            generation_settings = GptGenerationSettings(
                response_format=TriageStepResponse
            )
            creator.add(
                system=triage_step_response(self.language),
                assistant=triage_step_response_system(actions_str)
            )
            response = self.gpt_client.response(
                messages=creator.messages,
                generation_settings=generation_settings,
                preset=[]
            )
            return TriageStepResponse(**json.loads(response))

        actions_response = filter_actions(current_actions)
        choices_response = conversation_response()

        self.gpt_client.creator.clear()
        step_response = TriageStepResponse(
            available_actions=[action.name for action in actions_response],
            available_choices=choices_response.available_choices,
            response=choices_response.response
        )
        return step_response

    @staticmethod
    def __parse_actions(actions: list[Action] | None) -> str:
        if actions is None:
            return ''
        res = ''
        for i, action in enumerate(actions):
            res += f'{i + 1}. {action.name.value}\n'
            res += f'{action.description}\n'
            res += f'-----------------------\n'
        return res

    def __rollback(self):
        pass
