from abc import abstractmethod, ABC
from typing import Iterable

from src.application.generation_settings import GenerationSettings


class LlmClient(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def stream_response(self, messages: Iterable[object], generation_settings: GenerationSettings):
        pass

    @abstractmethod
    def response(self, messages: Iterable[object], generation_settings: GenerationSettings):
        pass
