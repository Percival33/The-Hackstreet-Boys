from abc import abstractmethod
from typing import MutableSequence


class PromptCreator:
    def __init__(self):
        self._messages: MutableSequence[dict] = []

    @abstractmethod
    def add(
            self,
            system: str | None,
            user: str | None,
            assistant: str | None,
            **kwargs
    ):
        pass

    def clear(self):
        self.messages = []

    @property
    def messages(self) -> MutableSequence[dict]:
        return self._messages

    @messages.setter
    def messages(self, value: MutableSequence[dict]):
        self._messages = value
