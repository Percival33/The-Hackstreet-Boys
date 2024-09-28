from typing import Iterable

from src.application.prompt_creator import PromptCreator


class GptPromptCreator(PromptCreator):
    def __init__(self):
        super().__init__()

    def add(
            self,
            system: str | None = None,
            user: str | None = None,
            assistant: str | None = None,
            **kwargs
    ):
        if system is not None and system != '':
            self.messages.append({
                'role': 'system',
                'content': system
            })

        if user is not None and user != '':
            self.messages.append({
                'role': 'user',
                'content': user
            })

        if assistant is not None and assistant != '':
            self.messages.append({
                'role': 'assistant',
                'content': assistant
            })

    def add_prebuilt(self, messages: Iterable[dict]):
        try:
            for message in messages:
                if message['role'] in ['system', 'user', 'assistant'] and type(message['content']) is str:
                    self.messages.append(message)
                else:
                    raise Exception("Wrong message format")
        except Exception as e:
            logger.error(f"Adding prebuilt message in GptPromptCreator failed: {e}")
