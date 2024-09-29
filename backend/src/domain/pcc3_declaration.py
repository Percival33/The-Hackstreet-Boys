from dataclasses import dataclass, field, fields
from xsdata.models.datatype import XmlDate

def validate_date(date: str) -> str | None:
	try:
		y, m, d = date.split('-', 2)
		date = XmlDate(int(y), int(m), int(d))
		if date < XmlDate(2024, 1, 1):
			return 'Data musi być nowsza niż 2024-01-01'
	except Exception:
		return 'Data została podana w nieprawidłowej formie'
	return None

VALIDATION_LOGIC = {
	'data_dokonania_czynnosci': validate_date,
	'pesel': lambda x: 'pesel ma błędną ilość znaków' if len(x)!=11 else None

}

@dataclass
class RemainingField:
	name: str
	description: str | None = None
	rule: str | None = None
	error: str | None = None

@dataclass
class PCC3Declaration:
	kod_urzedu_skarbowego: str | None = field(metadata={"id": "KodUrzedu", "opis": "Nazwa urzędu skarbowego"}, default=None)
	data_dokonania_czynnosci: str | None = field(metadata={"id": "Data", "opis": "Data dokonania czynności w formacie YYYY-MM-DD"}, default=None)

	# FIZYCZNA
	pesel: str | None = field(metadata={"id": "PESEL"}, default=None)
	imie_pierwsze: str | None = field(metadata={"id": "ImiePierwsze", "opis": "Pierwsze imie"}, default=None)
	nazwisko: str | None = field(metadata={"id": "Nazwisko"}, default=None)
	data_urodzenia: str | None = field(metadata={"id": "DataUrodzenia"}, default=None)

	# NIEFIZYCZNA
	nip: str | None = field(metadata={"id": "NIP"}, default=None)
	pelna_nazwa: str | None = field(metadata={"id": "PelnaNazwa"}, default=None)
	skrocona_nazwa: str | None = field(metadata={"id": "SkroconaNazwa"}, default=None)

	# ADRES
	wojewodztwo: str | None = field(metadata={"id": "Wojewodztwo"}, default=None)
	powiat: str | None = field(metadata={"id": "Powiat"}, default=None)
	gmina: str | None = field(metadata={"id": "Gmina"}, default=None)
	ulica: str | None = field(metadata={"id": "Ulica"}, default=None)
	nr_domu: str | None = field(metadata={"id": "NrDomu"}, default=None)
	nr_lokalu: str | None = field(metadata={"id": "NrLokalu"}, default=None)
	miejscowosc: str | None = field(metadata={"id": "Miejscowosc"}, default=None)
	kod_pocztowy: str | None = field(metadata={"id": "KodPocztowy", "opis": "Kod pocztowy w formacie NN-NNN"}, default=None)

	# SZCZEGOLY
	podmiot: int | None = field(metadata={"id": "P_7", "opis": "Podmiot składający deklarację: 1 - podmiot zobowiązany solidarnie do zapłaty podatku, 5 - inny podmiot"}, default=None)
	przedmiot_opadatkowania: int | None = field(metadata={"id": "P_20",
														  "opis": "Przedmiot opodatkowania : 1 - umowa, 2 - zmiana umowy, 3 - orzeczenie sądu lub ugoda, 4 - inne"},
												default=None)
	miejsce_polozenia_rzeczy: int | None = field(metadata={"id": "P_21",
														   "opis": "Miejsce położenia rzeczy lub miejsce wykonywania prawa majątkowego: 0 - niewypełnione, 1 - terytorium RP, 2 - poza terytorium RP"},
												 default=0)
	miejsce_dokonania_czynnosci_prawnej: int | None = field(metadata={"id": "P_22",
																	  "opis": "Miejsce dokonania czynności cywilnoprawnej: 0 - niewypełnione, 1 -terytorium RP, 2 - poza terytorium RP"},
															default=0)
	opis_sytuacji: str | None = field(
		metadata={"id": "P_23", "opis": "Zwięzłe określenie treści i przedmiotu czynności cywilnoprawnej"},
		default=None)

	# 0.5%
	podstawa_opodatkowania_p05: int | None = field(metadata={"id": "P_49",
															"opis": "Podstawa opodatkowania(opodatkowana wg stawki podatku 0.5%) określona zgodnie z art. 6 ustawy (po zaokrągleniu do pełnych złotych)"},
												  default=None)

	@property
	def obliczony_podatek_czynnosci_p05(self) -> int:
		"""
		P_50
		:return: Obliczony należny podatek od czynności cywilnoprawnej (po zaokrągleniu do pełnych złotych) (opodatkowana wg stawki podatku 0.5%)
		"""
		val = self.podstawa_opodatkowania_p05 or 0.0
		return round(val * 0.005)

	# 1%
	podstawa_opodatkowania_p1: int | None = field(metadata={"id": "P_24",
															"opis": "Podstawa opodatkowania(opodatkowana wg stawki podatku 1%) określona zgodnie z art. 6 ustawy (po zaokrągleniu do pełnych złotych)"},
												  default=None)
	@property
	def obliczony_podatek_czynnosci_p1(self) -> int:
		"""
		P_25
		:return: Obliczony należny podatek od czynności cywilnoprawnej (po zaokrągleniu do pełnych złotych) (opodatkowana wg stawki podatku 1%)
		"""
		val = self.podstawa_opodatkowania_p1 or 0.0
		return round(val*0.01)

	# 2%
	podstawa_opodatkowania_p2: int | None = field(metadata={"id": "P_26",
															"opis": "Podstawa opodatkowania(opodatkowana wg stawki podatku 2%) określona zgodnie z art. 6 ustawy (po zaokrągleniu do pełnych złotych). Podstawa opodatkowania dla umowy sprzedaży jest większa lub równa 1000 PLN;"},
												  default=None)
	@property
	def obliczony_podatek_czynnosci_p2(self) -> int:
		"""
		P_27
		:return: Obliczony należny podatek od czynności cywilnoprawnej (po zaokrągleniu do pełnych złotych) (opodatkowana wg stawki podatku 2%)
		"""
		val = self.podstawa_opodatkowania_p2 or 0.0
		return round(val*0.02)

	@property
	def kwota_podatku(self) -> int:
		"""
		P_46
		:return: Kwota należnego podatku
		"""
		if self.procent_podatku is not None:
			if self.procent_podatku=='0.5':
				return round(self.obliczony_podatek_czynnosci_p05)
			if self.procent_podatku=='1':
				return round(self.obliczony_podatek_czynnosci_p1)
			else:
				return round(self.obliczony_podatek_czynnosci_p2)
		return 0
	@property
	def kwota_do_zaplaty(self) -> int:
		"""
		P_53
		:return: Kwota podatku do zapłaty
		"""
		return self.kwota_podatku

	@property
	def ilosc_zalocznikow(self) -> int:
		"""
		P_62
		:return: Informacja o załącznikach - Liczba dołączonych załączników PCC-3/A
		"""
		if self.podmiot is not None and self.podmiot==1:
			return 1
		return 0

	# FLAGI
	czy_fizyczna: bool | None = field(metadata={"id": "czy_fizyczna"}, default=None)
	procent_podatku: str | None = field(metadata={"id": "procent_podatku"}, default=None)

	def get_hidden_fields(self):
		f = set()
		if self.czy_fizyczna is not None:
			f.update( ['NIP', 'PelnaNazwa', 'SkroconaNazwa'] if self.czy_fizyczna else ['PESEL', 'ImiePierwsze', 'Nazwisko', 'DataUrodzenia'])
		if self.procent_podatku is not None:
			if self.procent_podatku == "0.5":
				l = ['P_26', 'P_24']
			elif self.procent_podatku == "1":
				l = ['P_26', 'P_49']
			else:
				l = ['P_24', 'P_49']
			f.update(l)
		return f

	def get_remaining_fields(self) -> list[RemainingField]:
		unfilled_fields = []
		hidden_fields = self.get_hidden_fields()
		for f in fields(self):
			value = getattr(self, f.name)
			errs = None
			if value is not None:
				errs = VALIDATION_LOGIC.get(f.name, lambda x: None)(value)
				if errs is None:
					continue
			_id = f.metadata.get("id", f.name)
			if _id in hidden_fields:
				continue
			description = f.metadata.get("opis")
			unfilled_fields.append(RemainingField(f.name, description, error=errs))
		return unfilled_fields
