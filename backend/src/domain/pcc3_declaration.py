from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date


class PCC3Declaration(BaseModel):
    data_dokonania_czynnosci: date = Field(..., alias="P4", description="DATA DOKONANIA CZYNNOŚCI")
    cel_zlozenia_deklaracji: int = Field(..., alias="P6", description="CEL ZŁOŻENIA DEKLARACJI")
    podmiot_skladajacy_deklaracje: int = Field(..., alias="P7", description="PODMIOT SKŁADAJĄCY DEKLARACJĘ")
    przedmiot_opodatkowania: int = Field(..., alias="P20", description="PRZEDMIOT OPODATKOWANIA")
    miejsce_polozenia_rzeczy: Optional[int] = Field(None, alias="P21", description="MIEJSCE POŁOŻENIA RZECZY LUB WYKONYWANIA PRAWA MAJĄTKOWEGO")
    miejsce_dokonania_czynnosci: Optional[int] = Field(None, alias="P22", description="MIEJSCE DOKONANIA CZYNNOŚCI CYWILNOPRAWNEJ")
    okreslenie_czynnosci: str = Field(..., alias="P23", description="ZWIĘZŁE OKREŚLENIE TREŚCI I PRZEDMIOTU CZYNNOŚCI CYWILNOPRAWNEJ")
    podstawa_opodatkowania: float = Field(..., alias="P26", description="PODSTAWA OPODATKOWANIA DLA UMOWY SPRZEDAŻY (w PLN, zaokrąglona do pełnych złotych)")
    obliczony_nalezny_podatek: Optional[float] = Field(None, alias="P27", description="OBLICZONY NALEŻNY PODATEK OD UMOWY SPRZEDAŻY (w PLN, zaokrąglony do pełnych złotych)")
    kwota_naleznego_podatku: Optional[float] = Field(None, alias="P46", description="KWOTA NALEŻNEGO PODATKU (w PLN, zaokrąglona do pełnych złotych)")
    kwota_podatku_do_zaplaty: Optional[float] = Field(None, alias="P53", description="KWOTA PODATKU DO ZAPŁATY (w PLN, zaokrąglona do pełnych złotych)")
    liczba_zalacznikow_pcc_3a: Optional[int] = Field(0, alias="P62", description="LICZBA DOŁĄCZONYCH ZAŁĄCZNIKÓW PCC-3/A")
