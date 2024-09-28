import uuid
from enum import Enum

import pydantic

from src.domain.action import Action, ActionName, ALL_ACTIONS


class MessageType(str, Enum):
    USER = "USER"
    SYSTEM = "SYSTEM"


class Message(pydantic.BaseModel):
    type: MessageType
    text: str
    choices: list[str] | None = None

    def __dict__(self) -> dict:
        return {
            "type": self.type.value,
            "text": self.text,
            "choices": self.choices
        }


class ConversationId:
    def __init__(self, value: str):
        self._value = uuid.UUID(value)

    @property
    def value(self) -> str:
        return str(self._value)

    @classmethod
    def generate(cls):
        return cls(str(uuid.uuid4()))

    def __eq__(self, other):
        if isinstance(other, ConversationId):
            return self._value == other._value
        return False

    def __hash__(self):
        return hash(self._value)


class Conversation:
    def __init__(
            self,
            conversation_id: ConversationId | None = None,
            messages: list[Message] | None = None,
            available_actions: list[Action] | None = None,
    ) -> None:
        self._conversation_id = conversation_id or ConversationId.generate()
        self._messages = messages or []
        self._available_actions = available_actions or ALL_ACTIONS

    @property
    def id(self) -> ConversationId:
        return self._conversation_id

    @property
    def messages(self) -> list[Message]:
        return self._messages

    @property
    def available_actions(self) -> list[ActionName]:
        return self._available_actions

    def append_message(self, message: Message) -> None:
        self._messages.append(message)

    @classmethod
    def from_initial_user_message(cls, message_text: str) -> "Conversation":
        return cls(messages=[Message(type=MessageType.USER, text=message_text)])

    def __str__(self):
        return f"{self._conversation_id} {self._messages}"

    def __dict__(self) -> dict:
        return {
            "conversation_id": self.id.value,
            "messages": [msg.__dict__() for msg in self._messages],
            "available_actions": [str(action) for action in self._available_actions],
        }
