from src.domain.action import ALL_ACTIONS
from src.domain.conversation import Conversation, Message, MessageType
from src.infrastructure.llm.triage.triage import Triage

triage = Triage(
    language='polski'
)
messages = [
    Message(
        type=MessageType.USER,
        text='Chcę wypełnić PCC',
        choices=None
    ),
    Message(
        type=MessageType.ASSISTANT,
        text='Jaka wersja PCC?',
        choices=[
            'PCC-1',
            'PCC-2',
            'PCC-3'
        ]
    ),
    Message(
        type=MessageType.USER,
        text='PCC-3',
        choices=None
    ),
]

if __name__ == '__main__':
    conversation_sample = Conversation()
    conversation_sample._available_actions = ALL_ACTIONS.values()
    _ = [conversation_sample.append_message(i) for i in messages]

    res = triage.step(conversation_sample)

    print(res)
