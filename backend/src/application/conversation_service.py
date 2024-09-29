from dataclasses import dataclass

from src.application.conversation_repository import ConversationRepository
from src.domain.conversation import Conversation, Message, MessageType, ConversationStatus
from src.domain.pcc3_declaration import RemainingField
from src.infrastructure.llm.forms.forms import FormsModel
from src.infrastructure.llm.triage.triage import Triage
from src.application.form_serializer import FormSerializer


class ConversationService:
    def __init__(
            self,
            conversations_repo: ConversationRepository,
            triage_service: Triage,
            form_serialization: FormSerializer,
            forms_model: FormsModel,
    ):
        self._repo = conversations_repo
        self._triage_service = triage_service
        self._form_serialzier = form_serialization
        self._forms_model = forms_model

    def process(self, conversation: Conversation) -> None:
        if conversation.status == ConversationStatus.FORM:
            self._process_form(conversation)
        elif conversation.status == ConversationStatus.GENERATION:
            self._generate_form(conversation)
        else:
            self._process_triage(conversation)

    def _process_form(self, conversation: Conversation) -> None:
        self._forms_model.ask_question(conversation)

    def _generate_form(self, conversation: Conversation):
        if not conversation.xml:
            xml = self._form_serialzier.serialize_pcc3(conversation.form)
            conversation.set_xml(xml)

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

        if action_to_perform is not None:
            self._forms_model.initialize_form(conversation)

        self._repo.save(conversation)
