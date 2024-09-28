from enum import StrEnum
import pydantic

from src.domain.descriptions.descriptions import *


class ActionName(StrEnum):
    PCC3 = "PCC3"
    SD3 = "SD"
    DN1 = "DN-1"
    DR1 = "DR-1"


class Action(pydantic.BaseModel):
    name: ActionName
    description: str
    user_description: str
    references: list[str]


ALL_ACTIONS = {
    ActionName.PCC3: Action(name=ActionName.PCC3, description=PCC3_DESCRIPTION,
                            user_description="Musisz wypelnić formularz podatku od czynności cywilnoprawnych PCC-3",
                            references=['https://www.podatki.gov.pl/pcc-sd/abc-pcc/',
                                        'https://klient-eformularz.mf.gov.pl/declaration/form/422f3471-b5cb-4f25-9f81-2f43c497ec51/section/0/6d15df00-5a05-414e-ab89-38a61264859e/0']),
    ActionName.SD3: Action(name=ActionName.SD3, description=SD3_DESCRIPTION,
                           user_description="Musisz wypelnić formularz od spadków i darowizn SD-3",
                           references=['https://www.podatki.gov.pl/pcc-sd/abc-sd/',
                                       'https://klient-eformularz.mf.gov.pl/declaration/form/f22375ae-d844-472f-b04f-2b1a32867599/section/0/7e4f6f28-b500-4b14-9307-42d09de776b4/0']),
    ActionName.DN1: Action(name=ActionName.DN1, description=DN1_DESCRIPTION,
                           user_description="Musisz wypelnić formularz od nieruchomości DN-1", references=[
            'https://www.podatki.gov.pl/podatki-i-oplaty-lokalne/podatek-od-nieruchomosci/']),
    ActionName.DR1: Action(name=ActionName.DR1, description=DR1_DESCRIPTION,
                           user_description="Musisz wypelnić formularz rolny DR-1",
                           references=['https://www.podatki.gov.pl/podatki-i-oplaty-lokalne/podatek-rolny/']),
}
