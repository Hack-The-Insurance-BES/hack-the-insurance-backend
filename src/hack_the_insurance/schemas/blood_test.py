from pydantic import BaseModel, Field


class BloodTestSchema(BaseModel):
    kind: str
    unit: str = Field(alias="Birim")
    result: float = Field(alias="Sonuç")
    reference: str = Field(alias="Referans")

    class Config:
        populate_by_name = True
