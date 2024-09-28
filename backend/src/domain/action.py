from enum import Enum

import pydantic


class ActionName(str, Enum):
    PCC3 = "PCC3"


class Action(pydantic.BaseModel):
    name: ActionName
    description: str
    user_description: str


ALL_ACTIONS = {
    ActionName.PCC3: Action(name=ActionName.PCC3, description="opis pcc3", user_description="Musisz wypelnic pcc3"),
}
