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
    podmiot: int | None = field(metadata={"id": "P_7"}, default=None)
    przedmiot_opadatkowania: int | None = field(metadata={"id": "P_20"}, default=None)
    opis_sytuacji: str | None = field(metadata={"id": "P_23"}, default=None)
    podstawa_opodatkowania: int | None = field(metadata={"id": "P_24"}, default=None)
    obliczony_podatek_czynnosci: int | None = field(metadata={"id": "P_25"}, default=None)
    kwota_podatku: int | None = field(metadata={"id": "P_46"}, default=None)
    kwota_do_zaplaty: int | None = field(metadata={"id": "P_53"}, default=None)
    ilosc_zalocznikow: int | None = field(metadata={"id": "P_62"}, default=None)

    def get_remaining_fields(self) -> list[RemainingField]:
        unfilled_fields = []
        for f in fields(self):
            value = getattr(self, f.name)
            if value is None:
                _id = f.metadata.get("id", f.name)
                unfilled_fields.append(RemainingField(_id, "test description"))
        return unfilled_fields
