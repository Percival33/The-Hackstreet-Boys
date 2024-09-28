from pydantic import BaseModel


class BaseRequest(BaseModel):
    pass


class MessageRequest(BaseRequest):
    conversation_id: str | None = None
    text: str


class FormRequest(BaseRequest):
    conversation_id: str
    text: str
