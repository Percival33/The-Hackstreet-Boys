import json
from dataclasses import fields
from enum import Enum
from typing import Union
import logging
from pydantic import BaseModel

from src.application.generation_settings import GptGenerationSettings
from src.domain.conversation import Conversation
from src.infrastructure.llm.expert.domain_expert import DomainExpert
from src.infrastructure.llm.expert.prompts import expert_choose_responder, expert_choose_responder_system
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.gpt_prompt_creator import GptPromptCreator
from src.infrastructure.llm.forms.prompts import forms_process_response, forms_ask_question, forms_initialize_form, \
    forms_initialize_form_user

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


class FormsModel:
    def __init__(self, language: str):
        self.language = language

    def initialize_form(self, conversation: Conversation) -> FieldFillSchema:
        schema = conversation.form.get_remaining_fields()
        creator = GptPromptCreator()
        gpt_client = GptClient()

        conversation_history = conversation.messages
        conversation_history_str = ''
        for message in conversation_history:
            conversation_history_str += f'[{message.type.value}]\n{message.text}\n\n'

        schema_str = ''
        for instance in schema:
            for field in fields(instance):
                field_name = field.name
                field_value = getattr(instance, field_name)
                schema_str += f'{field_name}: {field_value}\n'
            schema_str += "\n"
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

        for field in response.fields:
            field_number = field.field_number
            field_value = field.field_value
            print(f"Field number: {field_number}, Field value: {field_value}")
            print(schema[field_number - 1])
            print("\n\n")

        return response

    def ask_question(self, schema: dict, conversation: Conversation):
        last_prompt = conversation.messages[-1].text
        responder = self.choose_responder(last_prompt)
        if responder.model == Model.EXPERT:
            return self.expert_answer(conversation)
        elif responder.model == Model.FORMS:
            return self.form_question(schema, conversation)

    def expert_answer(self, conversation: Conversation):
        domain_expert = DomainExpert(self.language)
        return domain_expert.respond(conversation, 5)

    def choose_responder(self, prompt: str):
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

    def form_question(self, schema: dict, conversation: Conversation):
        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=AskQuestionSchema
        )
        creator.add(
            # user=self.conversation_history,
            assistant=forms_ask_question(self.language),
            system=str(schema)
        )

        response = gpt_client.response(
            messages=creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )
        response = json.loads(response)
        response = AskQuestionSchema(**response)
        return response

    def process_response(self, response: str, schema: dict) -> FieldFillSchema:
        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=FieldFillSchema
        )
        creator.add(
            user=response,
            assistant=forms_process_response(),
            system=str(schema)
        )

        response = gpt_client.response(
            messages=creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )

        response = json.loads(response)
        response = FieldFillSchema(**response)
        return response
