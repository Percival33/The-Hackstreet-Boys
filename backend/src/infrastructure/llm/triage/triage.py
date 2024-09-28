import json
from pydantic import BaseModel
from src.application.generation_settings import GptGenerationSettings
from src.domain.action import ActionName, ALL_ACTIONS, Action
from src.domain.conversation import Conversation, Message
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.gpt_prompt_creator import GptPromptCreator
from src.infrastructure.llm.triage.prompts import triage_step_action, triage_step_response_system, triage_step_response


class TriageStepResponse(BaseModel):
    available_actions: list[ActionName]
    available_choices: list[str]
    response: str


class TriageModelActions(BaseModel):
    available_actions: list[ActionName]


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

        def filter_actions(actions: list[Action]) -> TriageModelActions:
            creator = GptPromptCreator()
            generation_settings = GptGenerationSettings(
                response_format=TriageModelActions
            )
            creator.add(
                system=triage_step_action(actions_str),
                assistant=triage_step_action(self.language)
            )
            response = self.gpt_client.response(
                messages=self.gpt_client.creator.messages,
                generation_settings=generation_settings,
                preset=[]
            )
            creator.clear()
            return TriageModelActions(**json.loads(response))

        def get_response(actions: list[Action]) -> TriageStepResponse:
            creator = GptPromptCreator()
            generation_settings = GptGenerationSettings(
                response_format=TriageStepResponse
            )
            creator.add(
                system=triage_step_response(actions_str),
                assistant=triage_step_response_system(self.language)
            )
            return TriageStepResponse(**json.loads(response))

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
        # response = json.loads(response)
        # return TriageModelResponse(**response)

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
