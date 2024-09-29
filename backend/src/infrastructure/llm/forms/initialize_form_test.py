from src.domain.conversation import Conversation, Message, MessageType
from src.infrastructure.llm.forms.forms import FormsModel

forms = FormsModel(language='polski')

conversation = Conversation()

messages = [
    Message(
        type=MessageType.USER,
        text='Nazywam się Adam Kaniasty i chciałbym wypełnić formularz PCC-3',
    ),
    Message(
        type=MessageType.ASSISTANT,
        text='Podaj swój numer PESEL',
    ),
    Message(
        type=MessageType.USER,
        text='2115',
    ),
]

for message in messages:
    conversation.append_message(message)

# conversation.

if __name__ == '__main__':
    res = forms.initialize_form(conversation)
    print(res)
