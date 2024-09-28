from enum import Enum


class ActionName(str, Enum):
    PCC3 = "PCC3"
    NO_ACTION = "NO_ACTION"


ALL_ACTIONS = {
    ActionName.PCC3: "PCC3",
    ActionName.NO_ACTION: "no action",
}
