import json
from typing import Any, Union

from pydantic import BaseModel

from src.application.generation_settings import GptGenerationSettings
from src.infrastructure.llm.gpt_client import GptClient
from src.infrastructure.llm.prompts import forms_process_response


class ProcessedFieldSchema(BaseModel):
    field_number: int
    field_value: Union[str, int, float, bool]


class ProcessingSchema(BaseModel):
    fields: list[ProcessedFieldSchema]


class FormsModel:
    def __init__(self, conversation_history: list[str]):
        self.conversation_history = conversation_history
        self.client = GptClient()

    def initialize_form(self, schema: dict):
        pass

    def ask_question(self, schema: dict):
        pass

    def process_response(self, response: str, schema: dict) -> ProcessingSchema:
        generation_settings = GptGenerationSettings(
            response_format=ProcessingSchema
        )
        self.client.creator.add(
            user=response,
            assistant=forms_process_response(),
            system=str(schema)
        )

        response = self.client.response(
            messages=self.client.creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )

        response = json.loads(response)

        response = ProcessingSchema(**response)

        return response
