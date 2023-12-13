from pydantic import Field
from typing import Optional

from .base import BaseDocument
from ..schemas.gpt_response import GptResponse


class BloodTestResult(BaseDocument):
    kind: str
    unit: str
    result: float
    reference: str
    gpt_response: Optional[GptResponse] = Field(default=None)
