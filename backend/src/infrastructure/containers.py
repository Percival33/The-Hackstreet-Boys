from openai import OpenAI

from src.infrastructure.chroma.chroma_client import get_chroma_client
from src.infrastructure.llm.triage.triage import Triage
from src.infrastructure.mongo.mongo_client import get_mongo_client
from src.infrastructure.mongo.mongo_conversation_repository import MongoConversationRepository
from src.infrastructure.settings import settings

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.infrastructure.api.routes",
        ]
    )

    chroma_client = providers.Singleton(get_chroma_client)

    openai_client = providers.Singleton(lambda: OpenAI(api_key=settings.openai_api_key))

    mongo_client = providers.Singleton(get_mongo_client)

    conversation_repository = providers.Factory(MongoConversationRepository, mongo_client)
