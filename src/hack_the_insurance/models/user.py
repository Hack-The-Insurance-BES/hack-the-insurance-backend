import datetime
from beanie import Link, Document
from pydantic import EmailStr, Field

from .blood_test import BloodTestResult


class User(Document):
    name: str
    height: float
    password: str
    email: EmailStr
    family_name: str
    birth_date: datetime.datetime
    blood_test_results: list[Link[BloodTestResult]] = Field(default=[])
    created_at: datetime.datetime = Field(default=datetime.datetime.now())
    updated_at: datetime.datetime = Field(default=datetime.datetime.now())
