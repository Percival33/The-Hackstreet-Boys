from openai import OpenAI

from src.application.conversation_service import ConversationService
from src.infrastructure.chroma.chroma_client import get_chroma_client
from src.infrastructure.llm.triage.triage import Triage
from src.infrastructure.mongo.mongo_client import get_mongo_client
from src.infrastructure.mongo.mongo_conversation_repository import MongoConversationRepository
from src.infrastructure.settings import settings
from src.infrastructure.llm.forms.forms import FormsModel

from dependency_injector import containers, providers

from src.infrastructure.xml.xml_serializer import XmlSerializer


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

    form_serialzier = providers.Factory(XmlSerializer)

    triage_service = providers.Factory(Triage, "PL")
    forms_model = providers.Factory(FormsModel, "PL")

    conversation_service = providers.Factory(ConversationService, conversation_repository, triage_service,form_serialzier, forms_model)
