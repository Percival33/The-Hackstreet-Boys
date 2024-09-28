from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, UploadFile, Depends, status, HTTPException, BackgroundTasks

from src.infrastructure.api.responses import BaseResponse
from src.infrastructure.containers import Container

router = APIRouter()


@router.get("/hc", response_model=BaseResponse)
@inject
def some_endpoint() -> BaseResponse:
    return BaseResponse()
