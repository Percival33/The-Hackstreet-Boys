from abc import abstractmethod, ABC
from src.domain.pcc3_declaration import PCC3Declaration


class FormSerializer(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def serialize_pcc3(self, declaration: PCC3Declaration) -> str:
		pass
