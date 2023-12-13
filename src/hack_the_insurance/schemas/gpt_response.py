import datetime
from pydantic import BaseModel, Field


class GptResponse(BaseModel):
    response: str
    token_usage: int
    total_cost: float
    at: datetime.datetime = Field(default=datetime.datetime.now())
