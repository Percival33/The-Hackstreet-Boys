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
    if request.conversation_id is None:
        conversation = Conversation.from_initial_user_message(request.text)
    else:
        conversation = conversation_repo.find(ConversationId(request.conversation_id))
        conversation.append_message(Message(type=MessageType.USER, text=request.text))

    if conversation.status != ConversationStatus.TRIAGE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Conversation not in triage stage")

    conversation_service.process(conversation)

    return ConversationResponse.from_conversation(conversation)


@router.post("/form", response_model=ConversationResponse)
@inject
def form_completion(
        request: FormRequest,
        conversation_service: ConversationService = Depends(Provide[Container.conversation_service]),
        conversation_repo: ConversationRepository = Depends(Provide[Container.conversation_repository]),
) -> ConversationResponse:
    conversation = conversation_repo.find(ConversationId(request.conversation_id))

    if conversation.status != ConversationStatus.FORM:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Conversation not in form stage")

    conversation_service.process(conversation)

    return ConversationResponse.from_conversation(conversation)