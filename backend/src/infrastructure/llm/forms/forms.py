import json
from typing import Union

from pydantic import BaseModel

from src.application.generation_settings import GptGenerationSettings
from src.domain.conversation import Conversation
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.prompts import forms_process_response, forms_ask_question


class AskQuestionSchema(BaseModel):
    message: str
    answered_fields: list[int]


class ProcessedFieldSchema(BaseModel):
    field_number: int
    field_value: Union[str, int, float, bool]


class ProcessingSchema(BaseModel):
    fields: list[ProcessedFieldSchema]


class FormsModel:
    def __init__(self,  language: str):
        self.gpt_client = GptClient()
        self.language = language

    def initialize_form(self, conversation: Conversation):
        pass

    def ask_question(self, schema: dict):
        generation_settings = GptGenerationSettings(
            response_format=AskQuestionSchema
        )
        self.gpt_client.creator.add(
            user=None,
            assistant=forms_ask_question(self.language),
            system=str(schema)
        )

        response = self.gpt_client.response(
            messages=self.gpt_client.creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )
        self.gpt_client.creator.clear()
        response = json.loads(response)
        response = AskQuestionSchema(**response)
        return response

    def process_response(self, response: str, schema: dict) -> ProcessingSchema:
        generation_settings = GptGenerationSettings(
            response_format=ProcessingSchema
        )
        self.gpt_client.creator.add(
            user=response,
            assistant=forms_process_response(),
            system=str(schema)
        )

        response = self.gpt_client.response(
            messages=self.gpt_client.creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )
        self.gpt_client.creator.clear()

        response = json.loads(response)
        response = ProcessingSchema(**response)
        return response
