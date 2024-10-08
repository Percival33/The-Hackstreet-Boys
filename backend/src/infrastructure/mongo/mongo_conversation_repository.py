import logging
from typing import Mapping, Any

from pymongo import MongoClient

from src.application.conversation_repository import ConversationRepository
from src.domain.action import ALL_ACTIONS
from src.domain.conversation import Conversation, ConversationId, MessageType, Message, ConversationStatus
from src.domain.pcc3_declaration import PCC3Declaration
from src.infrastructure.settings import settings

logger = logging.getLogger(__name__)


class MongoConversationRepository(ConversationRepository):
    _COLLECTION_NAME = "conversations"

    def __init__(self, mongo_client: MongoClient) -> None:
        self._mongo_client = mongo_client
        self._db = self._mongo_client[settings.mongo.db_name]
        self._conversations = self._db[self._COLLECTION_NAME]

    def save(self, conversation: Conversation):
        logger.info("Saving conversation %s", conversation.id)

        self._conversations.update_one(
            {"conversation_id": conversation.id.value},
            {"$set": conversation.__dict__()},
            upsert=True,
        )

    def find(self, conversation_id: ConversationId) -> Conversation | None:
        conversation = self._conversations.find_one({"conversation_id": conversation_id.value})
        if not conversation:
            return None

        return self._map_collection_to_conversation(conversation)

    def find_all(self) -> list[Conversation]:
        all_conversations = self._conversations.find({})
        return [
            self._map_collection_to_conversation(conversation) for conversation in all_conversations
        ]

    @staticmethod
    def _map_collection_to_conversation(collection: Mapping[str, Any]) -> Conversation:
        available_actions = [ALL_ACTIONS[action_name] for action_name in collection["available_actions"]]

        return Conversation(
            conversation_id=ConversationId(collection["conversation_id"]),
            messages=[Message(
                type=MessageType[msg["type"]],
                text=msg["text"],
                choices=msg.get("choices"),
                action_to_perform=msg.get("action_to_perform"),
            ) for msg in collection["messages"]],
            status=ConversationStatus[collection["status"]],
            available_actions=available_actions,
            form=PCC3Declaration(**collection["pcc3_form"]),
        )
