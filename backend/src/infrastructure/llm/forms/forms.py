import json
from dataclasses import fields
from enum import Enum
from typing import Union, Literal
import logging
from pydantic import BaseModel

from src.application.generation_settings import GptGenerationSettings
from src.domain.conversation import Conversation
from src.infrastructure.llm.expert.domain_expert import DomainExpert
from src.infrastructure.llm.expert.prompts import expert_choose_responder, expert_choose_responder_system
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.gpt_prompt_creator import GptPromptCreator
from src.infrastructure.llm.forms.prompts import forms_process_response, forms_ask_question, forms_initialize_form, \
    forms_initialize_form_user, forms_is_individual, forms_tax_rate

logger = logging.getLogger(__name__)


class AskQuestionSchema(BaseModel):
    message: str
    answered_fields: list[int]


class ProcessedFieldSchema(BaseModel):
    field_number: int
    field_value: Union[str, int, float, bool]


class FieldFillSchema(BaseModel):
    fields: list[ProcessedFieldSchema]


class Model(Enum):
    EXPERT = "expert"
    FORMS = "forms"


class ChooseModelSchema(BaseModel):
    model: Model


class IsIndividualSchema(BaseModel):
    user_type: Literal["individual", "company", "unknown"]


class FormsModel:
    def __init__(self, language: str):
        self.language = language

    def initialize_form(self, conversation: Conversation) -> FieldFillSchema:
        schema = conversation.form.get_remaining_fields()
        creator = GptPromptCreator()
        gpt_client = GptClient()

        conversation_history_str = self.get_conversation_history(conversation)

        schema_str = self.parse_schema(schema)

        creator.add(
            system=conversation_history_str,
            assistant=forms_initialize_form(),
            user=forms_initialize_form_user(schema_str)
        )

        generation_settings = GptGenerationSettings(
            response_format=FieldFillSchema
        )

        response = gpt_client.response(
            messages=creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )

        response = json.loads(response)
        response = FieldFillSchema(**response)

        return response

    def ask_question(self, conversation: Conversation):
        last_prompt = conversation.messages[-1].text
        responder = self.choose_responder(last_prompt)
        if responder.model == Model.EXPERT:
            return self.expert_answer(conversation)
        elif responder.model == Model.FORMS:
            return self.form_question(conversation)

    def expert_answer(self, conversation: Conversation):
        domain_expert = DomainExpert(self.language)
        return domain_expert.respond(conversation, 5)

    @staticmethod
    def choose_responder(prompt: str):
        logger.info(f"Choosing responder for prompt: {prompt}")
        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=ChooseModelSchema
        )
        creator.add(
            user=prompt,
            assistant=expert_choose_responder(),
            system=expert_choose_responder_system()
        )
        response = gpt_client.response(
            messages=creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )
        response = json.loads(response)
        response = ChooseModelSchema(**response)
        return response

    def form_question(self, conversation: Conversation):
        schema = conversation.form.get_remaining_fields()
        schema_str = self.parse_schema(schema)
        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=AskQuestionSchema
        )
        creator.add(
            user=self.get_conversation_history(conversation),
            assistant=forms_ask_question(self.language),
            system=schema_str
        )

        response = gpt_client.response(
            messages=creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )
        response = json.loads(response)
        response = AskQuestionSchema(**response)
        return response

    def process_response(self, conversation: Conversation) -> FieldFillSchema:
        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=FieldFillSchema
        )
        creator.add(
            user=conversation.messages[-1].text,
            assistant=forms_process_response(),
            system=self.get_conversation_history(conversation)
        )

        response = gpt_client.response(
            messages=creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )

        response = json.loads(response)
        response = FieldFillSchema(**response)
        return response

    def is_individual(self, conversation: Conversation) -> IsIndividualSchema:
        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=IsIndividualSchema
        )
        creator.add(
            assistant=forms_is_individual(),
            system=self.get_conversation_history(conversation)
        )

        response = gpt_client.response(
            messages=creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )
        response = json.loads(response)
        response = IsIndividualSchema(**response)
        return response

    def tax_rate(self, conversation: Conversation) -> float:
        possible_values = [0.05, 0.1, 0.2]
        gpt_client = GptClient()

        response = gpt_client.assistant_response(
            prompt='Determine tax rate based on your knowledge',
            context=self.get_conversation_history(conversation),
            assistant_id='asst_AazFHWo1StCE7J2MqRHtYFvh',
            temperature=0.2,
        )
        response = float(response)
        if response > 1:
            response = response / 10
        if response not in possible_values:
            return 0.2
        return response

    @staticmethod
    def get_conversation_history(conversation: Conversation) -> str:
        conversation_history = conversation.messages
        conversation_history_str = ''
        for message in conversation_history:
            conversation_history_str += f'[{message.type.value}]\n{message.text}\n\n'
        return conversation_history_str

    @staticmethod
    def parse_schema(schema) -> str:
        schema_str = ''
        for field in schema:
            schema_str += f"Nazwa: {field.name}\n"

            if field.description:
                schema_str += f"Opis: {field.description}\n"

            if field.rule:
                schema_str += f"Reguła: {field.rule}\n"

            schema_str += "\n"
        return schema_str
