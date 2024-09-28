import datetime

from pydantic import BaseModel, computed_field

from src.infrastructure.settings import settings


class BaseResponse(BaseModel):
    pass
