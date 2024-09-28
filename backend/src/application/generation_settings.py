from typing import Any

from openai import NOT_GIVEN
from pydantic import BaseModel


class GenerationSettings(BaseModel):
    pass


class GptGenerationSettings(GenerationSettings):
    model: str = 'gpt-4o-2024-08-06'
    max_tokens: int = 4096
    temperature: float = 1.0
    top_p: float = .95
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    response_format: Any = NOT_GIVEN
