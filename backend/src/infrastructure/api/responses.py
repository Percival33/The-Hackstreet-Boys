from pydantic import BaseModel

from src.domain.conversation import Conversation, Message


class BaseResponse(BaseModel):
    pass


class MessageResponse(BaseResponse):
    type: str
    text: str
    choices: list[str] | None = None


class ConversationResponse(BaseResponse):
    conversation_id: str
    messages: list[MessageResponse]

    @classmethod
    def from_conversation(cls, conversation: Conversation) -> "ConversationResponse":
        return ConversationResponse(
            conversation_id=conversation.id.value,
            messages=[
                MessageResponse(
                    type=message.type,
                    text=message.text,
                    choices=message.choices
                ) for message in conversation.messages
            ]
        )
