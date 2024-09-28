import uuid
from dataclasses import dataclass
from enum import Enum


class MessageType(str, Enum):
    USER = "USER"
    SYSTEM = "SYSTEM"


@dataclass(frozen=True)
class Message:
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
    def __init__(self, conversation_id: ConversationId | None = None, messages: list[Message] | None = None) -> None:
        self._conversation_id = conversation_id or ConversationId.generate()
        self._messages = messages or []

    @property
    def id(self) -> ConversationId:
        return self._conversation_id

    @property
    def messages(self) -> list[Message]:
        return self._messages

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
            "messages": [msg.__dict__() for msg in self._messages]
        }
