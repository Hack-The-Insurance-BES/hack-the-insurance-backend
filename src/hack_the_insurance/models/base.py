import datetime
from pydantic import Field
from beanie import Document


class BaseDocument(Document):
    created_at: datetime.datetime = Field(default=datetime.datetime.now())
    updated_at: datetime.datetime = Field(default=datetime.datetime.now())
