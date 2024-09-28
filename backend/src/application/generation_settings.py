from pydantic import BaseModel


class GenerationSettings(BaseModel):
    pass


class GptGenerationSettings(GenerationSettings):
    model: str = 'gpt-4o'
    max_tokens: int = 4096
    temperature: float = 1.0
    top_p: float = .95
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
