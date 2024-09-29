import dataclasses

from pydantic import BaseModel

from src.domain.action import ALL_ACTIONS
from src.domain.conversation import Conversation, Message


class BaseResponse(BaseModel):
    pass


class MessageResponse(BaseResponse):
    type: str
    text: str
    choices: list[str] | None = None
    action_to_perform: dict | None = None


class ConversationResponse(BaseResponse):
    conversation_id: str
    messages: list[MessageResponse]
    form: dict

    @classmethod
    def from_conversation(cls, conversation: Conversation) -> "ConversationResponse":
        form = dataclasses.asdict(conversation.form)
        hidden_fields = conversation.form.get_hidden_fields()
        return ConversationResponse(
            conversation_id=conversation.id.value,
            messages=[
                MessageResponse(
                    type=message.type,
                    text=message.text,
                    choices=message.choices,
                    action_to_perform={
                        "name": message.action_to_perform.name,
                        "description": ALL_ACTIONS[message.action_to_perform].user_description,
                        "references": ALL_ACTIONS[message.action_to_perform].references,
                    } if message.action_to_perform else None,
                ) for message in conversation.messages
            ],
            form={x: form[x] for x in form if x not in hidden_fields},
        )
