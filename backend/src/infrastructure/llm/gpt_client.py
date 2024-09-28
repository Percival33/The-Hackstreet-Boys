from typing import Tuple, Iterable, Generator

from openai import OpenAI

from backend.src.application.generation_settings import GptGenerationSettings
from backend.src.application.llm_client import LlmClient


class GptClient(LlmClient):
    def __init__(self):
        super().__init__()
        self.client = OpenAI()

    def stream_response(
            self,
            messages: Iterable[dict],
            generation_settings: GptGenerationSettings

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
            generation_settings: GptGenerationSettings
    ) -> str | None:
        try:
            response = self.client.chat.completions.create(
                model=generation_settings.model,
                max_tokens=generation_settings.max_tokens,
                temperature=generation_settings.temperature,
                top_p=generation_settings.top_p,
                frequency_penalty=generation_settings.frequency_penalty,
                presence_penalty=generation_settings.presence_penalty,
                messages=messages
            )
        except Exception as e:
            raise RuntimeError(f"Invalid openai reqeust: {e}")

        return response.choices[0].message.content
