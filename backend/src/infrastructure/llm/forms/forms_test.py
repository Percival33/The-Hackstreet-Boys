import dotenv
from src.domain.conversation import Conversation, Message, MessageType
from src.infrastructure.llm.forms.forms import FormsModel

dotenv.load_dotenv()

forms = FormsModel(
    language='polski'
)

system = '''Numer pola: 4
Nazwa: DATA DOKONANIA CZYNNOŚCI
Obowiązkowe? Tak Typ: Data
Opis: Data dokonania czynności nie może być wcześniejsza niż 01.01.2024 r. i nie może być
późniejsza niż data złożenia deklaracji
Reguła: data dokonania czynności jest większa lub równa 01.01.2024 r. i jest mniejsza lub równa
dacie złożenia deklaracji
P4>=01.01.2024 ORAZ P4<=data złożenia

Numer pola: 6
Nazwa: KWOTA TRANSAKCJI
Obowiązkowe? Tak Typ: Rzeczywiste
Opis: Kwota transakcji
Reguła: kwota jest większa od 0
P6=1

Numer pola: 7
Nazwa: PODMIOT SKŁADAJĄCY DEKLARACJĘ
Obowiązkowe? Tak Typ: Całkowite
Opis: Podmiot składający deklarację musi przyjmować wartość: 1 (podmiot zobowiązany solidarnie
do zapłaty podatku), lub 5 (inny podmiot).
Reguła: podmiot składający deklarację jest równy: 1 (podmiot zobowiązany solidarnie do zapłaty
podatku) lub 5 (inny podmiot)
P7=1 LUB P7=5'''

schema = {}

conversation = Conversation()
messages = [
    Message(
        type=MessageType.USER,
        text='Jak zapłacić podatek rolny?',
        choices=None
    ),
]

for message in messages:
    conversation.append_message(message)

if __name__ == '__main__':
    res = forms.ask_question(schema, conversation)
    print(res)
