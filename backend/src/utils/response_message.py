from pydantic import BaseModel
from typing import Optional


class ResponseModel(BaseModel):
    index: list[int]
    columns: list[str]
    data: list[str | int]


def response_message(
    message: str,
    success: bool,
    response_data: Optional[ResponseModel] = None,
):
    return {
        "message": message,
        "success": success,
        "response_data": response_data,
    }
