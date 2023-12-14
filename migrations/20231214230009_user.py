import os, sys

import beanie

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

import json
import datetime
from beanie import free_fall_migration

from src.hack_the_insurance.models.user import User
from src.hack_the_insurance.models.blood_test import BloodTestResult
from src.hack_the_insurance.schemas.blood_test import BloodTestSchema


class Forward:
    @free_fall_migration(document_models=[User, BloodTestResult])
    async def default_creations(self, session):
        print(os.getcwd())
        with open(f"{os.getcwd()}/migrations/static/mock_blood_test.json") as f:
            raw_blood_test_results = json.load(f)["Tam Kan Sayımı (Hemogram)"]

        blood_test_date = datetime.datetime.strptime(
            raw_blood_test_results["Tarih"], "%d.%m.%Y"
        )

        default_user = User(
            id=beanie.PydanticObjectId(),
            name="Furkan Melih",
            family_name="Ercan",
            height=1.78,
            password="test",
            email="furkanmelihercan.98@gmail.com",
            birth_date=datetime.datetime(year=1998, day=30, month=8),
            blood_test_results=[
                BloodTestResult(
                    id=beanie.PydanticObjectId(),
                    **BloodTestSchema(
                        **results, kind=result_kind, test_at=blood_test_date
                    ).model_dump()
                )
                for result_kind, results in raw_blood_test_results["Sonuçlar"].items()
            ],
        )
        print(default_user.id)
        await default_user.replace(session=session)


class Backward:
    @free_fall_migration(document_models=[User, BloodTestResult])
    async def revert_default_creations(self, session):
        pass
