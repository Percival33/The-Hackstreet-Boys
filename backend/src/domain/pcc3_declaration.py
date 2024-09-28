from dataclasses import dataclass, field, fields


@dataclass
class RemainingField:
    name: str
    description: str


@dataclass
class PCC3Declaration:
    kod_urzedu_skarbowego: str | None = field(metadata={"id": "KodUrzedu"}, default=None)
    pesel: str | None = field(metadata={"id": "PESEL"}, default=None)
    imie_pierwsze: str | None = field(metadata={"id": "ImiePierwsze"}, default=None)
    nazwisko: str | None = field(metadata={"id": "Nazwisko"}, default=None)
    data_urodzenia: str | None = field(metadata={"id": "DataUrodzenia"}, default=None)
    wojewodztwo: str | None = field(metadata={"id": "Wojewodztwo"}, default=None)
    powiat: str | None = field(metadata={"id": "Powiat"}, default=None)
    gmina: str | None = field(metadata={"id": "Gmina"}, default=None)
    ulica: str | None = field(metadata={"id": "Ulica"}, default=None)
    nr_domu: str | None = field(metadata={"id": "NrDomu"}, default=None)
    nr_lokalu: str | None = field(metadata={"id": "NrLokalu"}, default=None)
    miejscowosc: str | None = field(metadata={"id": "Miejscowosc"}, default=None)
    kod_pocztowy: str | None = field(metadata={"id": "KodPocztowy"}, default=None)
    podmiot: int | None = field(metadata={"id": "P_7", "opis": "Podmiot składający deklarację"}, default=None)
    przedmiot_opadatkowania: int | None = field(metadata={"id": "P_20",
                                                          "opis": "Przedmiot opodatkowania : 1 - umowa, 2 - zmiana umowy, 3 - orzeczenie sądu lub ugoda, 4 - inne"},
                                                default=None)
    opis_sytuacji: str | None = field(
        metadata={"id": "P_23", "opis": "Zwięzłe określenie treści i przedmiotu czynności cywilnoprawnej"},
        default=None)
    podstawa_opodatkowania: int | None = field(metadata={"id": "P_24",
                                                         "opis": "Podstawa opodatkowania określona zgodnie z art. 6 ustawy (po zaokrągleniu do pełnych złotych)"},
                                               default=None)
    obliczony_podatek_czynnosci: int | None = field(metadata={"id": "P_25",
                                                              "opis": "bliczony należny podatek od czynności cywilnoprawnej (po zaokrągleniu do pełnych złotych)"},
                                                    default=None)
    kwota_podatku: int | None = field(metadata={"id": "P_46", "opis": "Kwota należnego podatku"}, default=None)
    kwota_do_zaplaty: int | None = field(metadata={"id": "P_53", "opis": "Kwota podatku do zapłaty"}, default=None)
    ilosc_zalocznikow: int | None = field(
        metadata={"id": "P_62", "opis": "Informacja o załącznikach - Liczba dołączonych załączników PCC-3/A"},
        default=None)

    def get_remaining_fields(self) -> list[RemainingField]:
        unfilled_fields = []
        for f in fields(self):
            value = getattr(self, f.name)
            if value is None:
                _id = f.metadata.get("id", f.name)
                description = f.metadata.get("opis", "Brak opisu")
                unfilled_fields.append(RemainingField(_id, description))
        return unfilled_fields
