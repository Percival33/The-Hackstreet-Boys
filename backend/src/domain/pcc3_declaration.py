from dataclasses import dataclass, field, fields
from importlib.metadata import metadata


@dataclass
class RemainingField:
	name: str
	description: str | None = None
	rule: str | None = None

@dataclass
class PCC3Declaration:
	kod_urzedu_skarbowego: str | None = field(metadata={"id": "KodUrzedu"}, default=None)

	# FIZYCZNA
	pesel: str | None = field(metadata={"id": "PESEL"}, default=None)
	imie_pierwsze: str | None = field(metadata={"id": "ImiePierwsze"}, default=None)
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
	kod_pocztowy: str | None = field(metadata={"id": "KodPocztowy"}, default=None)

	# SZCZEGOLY
	podmiot: int | None = field(metadata={"id": "P_7", "opis": "Podmiot składający deklarację"}, default=None)
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
	podstawa_opodatkowania_p05: int | None = field(metadata={"id": "P_40",
															"opis": "Podstawa opodatkowania(opodatkowana wg stawki podatku 0.5%) określona zgodnie z art. 6 ustawy (po zaokrągleniu do pełnych złotych)"},
												  default=None)
	obliczony_podatek_czynnosci_p05: int | None = field(metadata={"id": "p_41",
																 "opis": "Obliczony należny podatek od czynności cywilnoprawnej (po zaokrągleniu do pełnych złotych) (opodatkowana wg stawki podatku 0.5%)"},
													   default=None)
	# 1%
	podstawa_opodatkowania_p1: int | None = field(metadata={"id": "P_24",
															"opis": "Podstawa opodatkowania(opodatkowana wg stawki podatku 1%) określona zgodnie z art. 6 ustawy (po zaokrągleniu do pełnych złotych)"},
												  default=None)
	obliczony_podatek_czynnosci_p1: int | None = field(metadata={"id": "P_25",
																 "opis": "Obliczony należny podatek od czynności cywilnoprawnej (po zaokrągleniu do pełnych złotych) (opodatkowana wg stawki podatku 1%)"},
													   default=None)

	# 2%
	podstawa_opodatkowania_p2: int | None = field(metadata={"id": "P_26",
															"opis": "Podstawa opodatkowania(opodatkowana wg stawki podatku 2%) określona zgodnie z art. 6 ustawy (po zaokrągleniu do pełnych złotych). Podstawa opodatkowania dla umowy sprzedaży jest większa lub równa 1000 PLN;"},
												  default=None)
	obliczony_podatek_czynnosci_p2: int | None = field(metadata={"id": "P_27",
																 "opis": "Obliczony należny podatek od czynności cywilnoprawnej (po zaokrągleniu do pełnych złotych) (opodatkowana wg stawki podatku 2%)"},
													   default=None)

	kwota_podatku: int | None = field(metadata={"id": "P_46", "opis": "Kwota należnego podatku"}, default=None)
	kwota_do_zaplaty: int | None = field(metadata={"id": "P_53", "opis": "Kwota podatku do zapłaty"}, default=None)
	ilosc_zalocznikow: int | None = field(
		metadata={"id": "P_62", "opis": "Informacja o załącznikach - Liczba dołączonych załączników PCC-3/A"},
		default=0)

	# FLAGI
	czy_fizyczna: bool | None = field(metadata={"id": "czy_fizyczna"}, default=None)
	procent_podatku: str | None = field(metadata={"id": "procent_podatku"}, default=None)

	def get_remaining_fields(self) -> list[RemainingField]:
		unfilled_fields = []
		for f in fields(self):
			value = getattr(self, f.name)
			if value is not None:
				continue
			_id = f.metadata.get("id", f.name)
			if _id in ['P_27', 'P_25', 'P_46', 'P_53', 'P_62', 'P_41']:
				continue
			if self.czy_fizyczna is not None:
				if self.czy_fizyczna and _id in ['NIP', 'PelnaNazwa', 'SkroconaNazwa']:
					continue
				if not self.czy_fizyczna and _id in ['PESEL', 'ImiePierwsze', 'Nazwisko', 'DataUrodzenia']:
					continue
			if self.procent_podatku is not None:
				if self.procent_podatku=='0.5' and _id in ['P_26', 'P_27', 'P_24', 'P_25']:
					continue
				if self.procent_podatku=='1' and _id in ['P_26', 'P_27', 'P_40', 'P_41']:
					continue
				if self.procent_podatku=='2' and _id in ['P_24', 'P_25', 'P_40', 'P_41']:
					continue

			description = f.metadata.get("opis")
			unfilled_fields.append(RemainingField(_id, description))
		return unfilled_fields
