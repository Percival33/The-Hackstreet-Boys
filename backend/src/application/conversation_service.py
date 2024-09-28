from src.application.conversation_repository import ConversationRepository
from src.domain.conversation import Conversation, Message, MessageType, ConversationStatus
from src.infrastructure.llm.triage.triage import Triage


class ConversationService:
    def __init__(
        self,
        conversations_repo: ConversationRepository,
        triage_service: Triage,
    ):
        self._repo = conversations_repo
        self._triage_service = triage_service

    def process(self, conversation: Conversation) -> None:
        if conversation.status == ConversationStatus.FORM:
            self._process_form(conversation)
        else:
            self._process_triage(conversation)

    def _process_form(self, conversation: Conversation) -> None:
        pass

    def _process_triage(self, conversation: Conversation) -> None:
        result = self._triage_service.step(conversation)
        conversation.set_available_actions(result.available_actions)

        action_to_perform = None
        if len(conversation.available_actions) == 1:
            conversation.finish_triage()
            action_to_perform = conversation.available_actions[0].name

        conversation.append_message(
            Message(
                type=MessageType.ASSISTANT,
                text=result.response,
                choices=result.available_choices,
                action_to_perform=action_to_perform
            )
        )

        self._repo.save(conversation)
