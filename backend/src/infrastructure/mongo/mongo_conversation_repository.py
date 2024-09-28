import logging
from typing import Mapping, Any

from pymongo import MongoClient

from src.application.conversation_repository import ConversationRepository
from src.domain.conversation import Conversation, ConversationId, MessageType, Message
from src.infrastructure.settings import settings

logger = logging.getLogger(__name__)


class MongoConversationRepository(ConversationRepository):
    _COLLECTION_NAME = "conversations"

    def __init__(self, mongo_client: MongoClient) -> None:
        self._mongo_client = mongo_client
        self._db = self._mongo_client[settings.mongo.db_name]
        self._notes = self._db[self._COLLECTION_NAME]

    def save(self, conversation: Conversation):
        logger.info("Saving conversation %s", conversation.id)

        self._notes.update_one(
            {"conversation_id": conversation.id.value},
            {"$set": conversation.__dict__()},
            upsert=True,
        )

    def find(self, conversation_id: ConversationId) -> Conversation | None:
        conversation = self._notes.find_one({"conversation_id": conversation_id.value})
        if not conversation:
            return None

        return self._map_collection_to_conversation(conversation)

    @staticmethod
    def _map_collection_to_conversation(collection: Mapping[str, Any]) -> Conversation:
        return Conversation(
            conversation_id=ConversationId(collection["conversation_id"]),
            messages=[Message(
                type=MessageType[msg["type"]],
                text=msg["text"],
                choices=msg["choices"]
            ) for msg in collection["messages"]],
        )
