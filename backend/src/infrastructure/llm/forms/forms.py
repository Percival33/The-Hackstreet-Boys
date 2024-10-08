import json
from enum import Enum
from typing import Union, Literal
import logging
from pydantic import BaseModel

from src.application.generation_settings import GptGenerationSettings
from src.domain.conversation import Conversation, MessageType
from src.infrastructure.llm.expert.domain_expert import DomainExpert
from src.infrastructure.llm.expert.prompts import expert_choose_responder, expert_choose_responder_system
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.gpt_prompt_creator import GptPromptCreator
from src.infrastructure.llm.forms.prompts import forms_process_response, forms_ask_question, forms_initialize_form, \
    forms_initialize_form_user, forms_is_individual

logger = logging.getLogger(__name__)


class AskQuestionSchema(BaseModel):
    message: str
    answered_fields: list[str]


class ProcessedFieldSchema(BaseModel):
    field_id: str
    field_value: Union[str, int, float, bool]


class FieldFillSchema(BaseModel):
    fields: list[ProcessedFieldSchema]


class Model(Enum):
    EXPERT = "expert"
    FORMS = "forms"
    IRRELEVANT = "irrelevant"


class ChooseModelSchema(BaseModel):
    model: Model


class IsIndividualSchema(BaseModel):
    user_type: Literal["individual", "company", "unknown"]


class CodeSchema(BaseModel):
    code: str


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

    def ask_question(self, conversation: Conversation) -> AskQuestionSchema | str | bool:
        if conversation.messages[-1].type == MessageType.ASSISTANT:
            return self.form_question(conversation)
        else:
            responder = self.choose_responder(conversation)
            if responder.model == Model.FORMS:
                return self.form_question(conversation)
            elif responder.model == Model.EXPERT:
                return self.expert_answer(conversation)
            elif responder.model == Model.IRRELEVANT:
                return False

    def expert_answer(self, conversation: Conversation) -> str:
        domain_expert = DomainExpert(self.language)
        return domain_expert.respond(conversation, 5)

    def choose_responder(self, conversation: Conversation) -> ChooseModelSchema:
        prompt = conversation.messages[-1].text
        logger.info(f"Choosing responder for prompt: {prompt}")

        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=ChooseModelSchema
        )
        creator.add(
            user=prompt,
            assistant=expert_choose_responder(),
            system=expert_choose_responder_system(self.get_conversation_history(conversation))
        )
        response = gpt_client.response(
            messages=creator.messages,
            generation_settings=generation_settings,
            preset=[]
        )
        response = json.loads(response)
        response = ChooseModelSchema(**response)
        return response

    def form_question(self, conversation: Conversation) -> AskQuestionSchema:
        schema = conversation.form.get_remaining_fields()
        schema_str = self.parse_schema(schema)
        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=AskQuestionSchema,
            temperature=0.7
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
        schema = conversation.form.get_remaining_fields()
        schema_str = self.parse_schema(schema)
        creator = GptPromptCreator()
        gpt_client = GptClient()
        generation_settings = GptGenerationSettings(
            response_format=FieldFillSchema,
            temperature=0.7
        )
        creator.add(
            user=self.get_conversation_history(conversation),
            assistant=forms_process_response(),
            system=schema_str
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

    def tax_rate(self, conversation: Conversation) -> str:
        possible_values = ["0.5", "1", "2"]
        gpt_client = GptClient()

        response = gpt_client.assistant_response(
            prompt='Determine tax rate based on your knowledge',
            context=self.get_conversation_history(conversation),
            assistant_id='asst_ZtTe7v9whhliZWQX9xOQewyn',
            temperature=0.2,
        )
        if response not in possible_values:
            return "2"
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
            if field.error:
                schema_str += f'Błędy wczesniejszego wypełnienia: {field.error}'

            schema_str += "\n"
        return schema_str

    @staticmethod
    def swap_for_enum(value: str) -> str:
        client = GptClient()
        assistant_id = 'asst_jhOguRuVIGb7n8R80GuRFR4p'
        res = client.assistant_response(
            prompt=value,
            assistant_id=assistant_id,
            temperature=1
        )
        if res is not None and len(res) == 4:
            return res
        else:
            creator = GptPromptCreator()
            creator.add(
                assistant='Extract the code of the tax office from the given text. Return only the code. ',
                user=res
            )
            res = client.response(
                messages=creator.messages,
                generation_settings=GptGenerationSettings(response_format=CodeSchema, temperature=.7),
            )
            res = json.loads(res)
            res = CodeSchema(**res).code
            if len(res) == 4:
                return res
            return '1435'  # remove default value
