import json
import logging
from enum import Enum

from pydantic import BaseModel
from src.application.generation_settings import GptGenerationSettings
from src.domain.action import ActionName, Action
from src.domain.conversation import Conversation
from src.infrastructure.llm.expert.domain_expert import DomainExpert
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.gpt_prompt_creator import GptPromptCreator
from src.infrastructure.llm.triage.prompts import triage_step_action, triage_step_response_system, triage_step_response, \
    triage_step_action_system

logger = logging.getLogger(__name__)


class TriageStepResponse(BaseModel):
    available_actions: list[ActionName]
    available_choices: list[str]
    response: str


class TriageModelActions(BaseModel):
    actions_to_remove: list[ActionName]


class TriageModelResponse(BaseModel):
    available_choices: list[str]
    response: str


class TriageExpert(Enum):
    DOMAIN = 'DOMAIN'
    SYSTEM = 'SYSTEM'


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
        # creator = GptPromptCreator()
        # creator.add_from_conversation(conversation.messages)

        # domain_expert = DomainExpert(self.language)

        # if choose_expert(conversation) == Expert.
        return self.prompt_user(conversation)

    def choose_expert(
            self,
            conversation: Conversation
    ) -> TriageStepResponse:
        pass

    def prompt_user(
            self,
            conversation: Conversation
    ) -> TriageStepResponse:
        creator = GptPromptCreator()
        creator.add_from_conversation(conversation.messages)
        current_actions = conversation.available_actions
        actions_str = self.__parse_actions(current_actions)

        initial_messages = creator.messages

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
            expert = DomainExpert(self.language)

            last_message = conversation.messages[-1].text

            chunks = expert.query_chroma(last_message, 5)

            context_str = '\n\n'.join(chunks)

            creator.add_prebuilt(initial_messages)
            generation_settings = GptGenerationSettings(
                response_format=TriageStepResponse
            )
            creator.add(
                assistant=triage_step_response(self.language),
                system=triage_step_response_system(actions_str, context_str)
            )
            response = self.gpt_client.response(
                messages=creator.messages,
                generation_settings=generation_settings,
                preset=[]
            )
            return TriageStepResponse(**json.loads(response))

        actions_response = filter_actions(current_actions)
        choices_response = conversation_response()
        step_response = TriageStepResponse(
            available_actions=[action.name for action in actions_response],
            available_choices=choices_response.available_choices,
            response=choices_response.response
        )
        logger.info(f"Actions to keep: {str([v.value for v in step_response.available_actions])}")
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
