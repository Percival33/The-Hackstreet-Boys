import logging
import uuid
from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, UploadFile, Depends, status, HTTPException, BackgroundTasks

from src.application.conversation_repository import ConversationRepository
from src.domain.conversation import Conversation, ConversationId, Message, MessageType
from src.infrastructure.api.requests import MessageRequest
from src.infrastructure.api.responses import BaseResponse, ConversationResponse
from src.infrastructure.containers import Container
from src.infrastructure.llm.triage.triage import Triage

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/conversation", response_model=ConversationResponse)
@inject
def start_conversation(
        request: MessageRequest,
        conversation_repo: ConversationRepository = Depends(Provide[Container.conversation_repository]),
        triage_service: Triage = Depends(Provide[Container.triage]),
) -> ConversationResponse:
    if request.conversation_id is None:
        conversation = Conversation.from_initial_user_message(request.text)
    else:
        conversation = conversation_repo.find(ConversationId(request.conversation_id))
        conversation.append_message(Message(type=MessageType.USER, text=request.text))

    result = triage_service.step(conversation)
    conversation_id = result.conversation_id.

    # process conversation
    conversation_repo.save(conversation)

    conversation_repo.save(conversation)
    return ConversationResponse.from_conversation(conversation)
