import dataclasses
import uuid
from enum import StrEnum

import pydantic

from src.domain.action import ActionName, ALL_ACTIONS, Action
from src.domain.pcc3_declaration import PCC3Declaration


class MessageType(StrEnum):
    USER = "USER"
    SYSTEM = "SYSTEM"
    ASSISTANT = "ASSISTANT"


class Message(pydantic.BaseModel):
    type: MessageType
    text: str
    choices: list[str] | None = None
    action_to_perform: ActionName | None = None


class ConversationStatus(StrEnum):
    TRIAGE = "TRIAGE"
    FORM = "FORM"
    GENERATION = "GENERATION"


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
            status: ConversationStatus | None = None,
            form: PCC3Declaration | None = None,
            generated_xml: str | None = None
    ) -> None:
        self._conversation_id = conversation_id or ConversationId.generate()
        self._messages = messages or []
        self._available_actions = available_actions or ALL_ACTIONS.values()
        self._status = status or ConversationStatus.TRIAGE
        self._pcc3_form = form or PCC3Declaration()
        self._generated_xml = generated_xml

    @property
    def id(self) -> ConversationId:
        return self._conversation_id

    @property
    def messages(self) -> list[Message]:
        return self._messages

    @property
    def available_actions(self) -> list[Action]:
        return self._available_actions

    @property
    def status(self) -> ConversationStatus:
        return self._status

    @property
    def form(self) -> PCC3Declaration:
        return self._pcc3_form

    @property
    def xml(self) -> str | None:
        return self._generated_xml

    def set_form(self, new_form: PCC3Declaration) -> None:
        self._pcc3_form = new_form

    def append_message(self, message: Message) -> None:
        self._messages.append(message)

    def finish_triage(self):
        self._status = ConversationStatus.FORM

    def finish_form_processing(self):
        self._status = ConversationStatus.GENERATION

    def set_xml(self, xml):
        self._generated_xml = xml

    def set_available_actions(self, actions: list[ActionName]) -> None:
        self._available_actions = [ALL_ACTIONS[action_name] for action_name in actions]

    def __str__(self):
        return f"{self._conversation_id} {self._messages} {self._available_actions}"

    def __dict__(self) -> dict:
        return {
            "conversation_id": self.id.value,
            "messages": [msg.model_dump() for msg in self._messages],
            "available_actions": [action.name for action in self._available_actions],
            "status": str(self._status),
            "pcc3_form": dataclasses.asdict(self._pcc3_form),
        }
