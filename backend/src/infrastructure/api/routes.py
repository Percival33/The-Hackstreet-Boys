import logging
import uuid
from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, UploadFile, Depends, status, HTTPException, BackgroundTasks

from src.application.conversation_repository import ConversationRepository
from src.application.conversation_service import ConversationService
from src.domain.conversation import Conversation, ConversationId, Message, MessageType, ConversationStatus
from src.infrastructure.api.requests import MessageRequest, FormRequest
from src.infrastructure.api.responses import BaseResponse, ConversationResponse
from src.infrastructure.containers import Container
from src.infrastructure.llm.triage.triage import Triage

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/conversation", response_model=ConversationResponse)
@inject
def conversation(
        request: MessageRequest,
        conversation_service: ConversationService = Depends(Provide[Container.conversation_service]),
        conversation_repo: ConversationRepository = Depends(Provide[Container.conversation_repository]),
) -> ConversationResponse:
    conversation = Conversation() if request.conversation_id is None \
        else conversation_repo.find(ConversationId(request.conversation_id))

    if request.text:
        conversation.append_message(Message(type=MessageType.USER, text=request.text))

    conversation_service.process(conversation)

    return ConversationResponse.from_conversation(conversation)


@router.get("/all_conversations", response_model=list[ConversationResponse])
@inject
def get_all_conversations(
        conversation_repo: ConversationRepository = Depends(Provide[Container.conversation_repository]),
) -> list[ConversationResponse]:
    return [
        ConversationResponse.from_conversation(conversation) for conversation in conversation_repo.find_all()
    ]
