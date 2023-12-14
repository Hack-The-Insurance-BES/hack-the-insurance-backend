import datetime

from pydantic import BaseModel, Field


class BloodTestSchema(BaseModel):
    kind: str
    result: float = Field(alias="Sonuç")
    test_at: datetime.datetime = Field(alias="Tarih")
    unit: str | None = Field(alias="Birim", default=None)
    reference: str | None = Field(alias="Referans", default=None)

    class Config:
        populate_by_name = True
