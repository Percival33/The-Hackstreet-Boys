from typing import Tuple, Iterable, Generator

from openai import OpenAI

from src.application.generation_settings import GptGenerationSettings
from src.application.llm_client import LlmClient
from src.infrastructure.llm.gpt_prompt_creator import GptPromptCreator


class GptClient(LlmClient):
    def __init__(self):
        super().__init__()
        self.client = OpenAI()
        self.creator = GptPromptCreator()

    def stream_response(
            self,
            messages: Iterable[dict],
            generation_settings: GptGenerationSettings,
            preset: Iterable[dict]

    ) -> Generator:
        response = self.client.chat.completions.create(
            model=generation_settings.model,
            max_tokens=generation_settings.max_tokens,
            temperature=generation_settings.temperature,
            top_p=generation_settings.top_p,
            frequency_penalty=generation_settings.frequency_penalty,
            presence_penalty=generation_settings.presence_penalty,
            messages=messages,
            stream=True
        )
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

    def response(
            self,
            messages: Iterable[dict],
            generation_settings: GptGenerationSettings,
            preset: Iterable[dict] | None = None
    ) -> str | None:
        try:
            if preset is not None:
                messages = [*preset, *messages]
            response = self.client.beta.chat.completions.parse(
                model=generation_settings.model,
                max_tokens=generation_settings.max_tokens,
                temperature=generation_settings.temperature,
                top_p=generation_settings.top_p,
                frequency_penalty=generation_settings.frequency_penalty,
                presence_penalty=generation_settings.presence_penalty,
                messages=messages,
                response_format=generation_settings.response_format
            )
        except Exception as e:
            raise RuntimeError(f"Invalid openai reqeust: {e}")

        return response.choices[0].message.content

    def triage_preset(self):
        pass
