import datetime
from pydantic import Field
from beanie import Document

from ..schemas.gpt_response import GptResponse


class BloodTestResult(Document):
    kind: str
    result: float
    test_at: datetime.datetime
    unit: str | None = Field(default=None)
    reference: str | None = Field(default=None)
    gpt_response: GptResponse | None = Field(default=None)
    created_at: datetime.datetime = Field(default=datetime.datetime.now())
    updated_at: datetime.datetime = Field(default=datetime.datetime.now())

    class Settings:
        name = "blood_test_result"
