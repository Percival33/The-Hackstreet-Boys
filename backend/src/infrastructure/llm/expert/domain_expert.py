from openai import OpenAI

from src.application.generation_settings import GptGenerationSettings
from src.domain.conversation import Conversation, Message, MessageType
from src.infrastructure.chroma.chroma_client import get_chroma_client
from src.infrastructure.llm.expert.prompts import expert_assistant, expert_system
from src.infrastructure.llm.forms.gpt_client import GptClient
from src.infrastructure.llm.forms.gpt_prompt_creator import GptPromptCreator
from src.infrastructure.settings import settings


class DomainExpert:
    def __init__(self, language: str):
        self.language = language

    def query_chroma(self, query: str, top_k: int):
        chroma = get_chroma_client()
        collection = chroma.get_collection("assistant")
        query_embedding = self.embed(query)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        documents = []
        for result in results['documents']:
            documents.extend(result)
        return documents

    def respond(self, conversation: Conversation, top_k: int):
        creator = GptPromptCreator()
        last_message = conversation.messages[-1]
        other_messages = conversation.messages[:-1]
        documents = self.query_chroma(last_message.text, top_k)
        client = GptClient()
        creator.add_from_conversation(other_messages)
        creator.add(
            system=expert_system(documents),
            user=last_message.text,
            assistant=expert_assistant(self.language),
        )
        generation_settings = GptGenerationSettings()
        res = client.response(
            generation_settings=generation_settings,
            messages=creator.messages
        )

        return res

    @staticmethod
    def embed(query: str):
        client = OpenAI(api_key=settings.openai_api_key)
        res = client.embeddings.create(
            input=[query],
            model='text-embedding-3-small',
        )
        return res.data[0].embedding


if __name__ == "__main__":
    expert = DomainExpert("polski")
    conversation = Conversation()
    message = Message(
        text="Czym jest wartość rynkowa",
        type=MessageType.USER
    )
    conversation.append_message(message)
    res = expert.respond(conversation, 5)
    print(res)
