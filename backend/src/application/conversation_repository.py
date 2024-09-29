import abc

from src.domain.conversation import Conversation, ConversationId


class ConversationRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, conversation: Conversation):
        pass

    @abc.abstractmethod
    def find(self, conversation_id: ConversationId) -> Conversation:
        pass

    @abc.abstractmethod
    def find_all(self) -> list[Conversation]:
        pass
