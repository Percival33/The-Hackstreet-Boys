from dataclasses import dataclass, field, fields


@dataclass
class PCC3Declaration:
    kod_urzedu_skarbowego: str = field(metadata={"id": "KodUrzedu"})
    pesel: str = field(metadata={"id": "PESEL"})
    imie_pierwsze: str = field(metadata={"id": "ImiePierwsze"})
    nazwisko: str = field(metadata={"id": "Nazwisko"})
    data_urodzenia: str = field(metadata={"id": "DataUrodzenia"})
    wojewodztwo: str = field(metadata={"id": "Wojewodztwo"})
    powiat: str = field(metadata={"id": "Powiat"})
    gmina: str = field(metadata={"id": "Gmina"})
    ulica: str = field(metadata={"id": "Ulica"})
    nr_domu: str = field(metadata={"id": "NrDomu"})
    nr_lokalu: str = field(metadata={"id": "NrLokalu"})
    miejscowosc: str = field(metadata={"id": "Miejscowosc"})
    kod_pocztowy: str = field(metadata={"id": "KodPocztowy"})
    podmiot: int = field(metadata={"id": "P_7"})
    przedmiot_opadatkowania: int = field(metadata={"id": "P_20"})
    opis_sytuacji: str = field(metadata={"id": "P_23"})
    podstawa_opodatkowania: int = field(metadata={"id": "P_24"})
    obliczony_podatek_czynnosci: int = field(metadata={"id": "P_25"})
    kwota_podatku: int = field(metadata={"id": "P_46"})
    kwota_do_zaplaty: int = field(metadata={"id": "P_53"})
    ilosc_zalocznikow: int = field(metadata={"id": "P_62"})

    def get_remaining_fields(self):
        unfilled_fields = []
        for f in fields(self):
            value = getattr(self, f.name)
            if value is None:
                unfilled_fields.append(f.metadata.get("id", f.name))
        return unfilled_fields
