import datetime
from typing import List
from beanie import Link
from pydantic import EmailStr, Field

from .base import BaseDocument
from .blood_test import BloodTestResult


class User(BaseDocument):
    name: str
    height: float
    password: str
    email: EmailStr
    birth_date: datetime.datetime
    blood_test_results: List[Link[BloodTestResult]] = Field(default=[])

