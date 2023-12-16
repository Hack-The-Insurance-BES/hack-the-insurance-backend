import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")

import json
import beanie
import datetime
from beanie import WriteRules
from beanie import free_fall_migration

from src.hack_the_insurance.models.user import User
from src.hack_the_insurance.models.blood_test import BloodTestResult
from src.hack_the_insurance.schemas.blood_test import BloodTestSchema


def read_and_retrieve_static_results() -> dict:
    with open(f"{os.getcwd()}/migrations/static/mock_blood_test.json") as f:
        raw_blood_test_results = json.load(f)["Tam Kan Sayımı (Hemogram)"]

    return raw_blood_test_results


class Forward:
    @free_fall_migration(document_models=[User, BloodTestResult])
    async def blood_test_result_migration(self, session):
        raw_blood_test_results = read_and_retrieve_static_results()
        blood_test_date = datetime.datetime.strptime(
            raw_blood_test_results["Tarih"], "%d.%m.%Y"
        )
        default_user = await User.find(
            {User.email: "furkanmelihercan.98@gmail.com"}
        ).first_or_none()
        if default_user is None:
            return

        default_user.blood_test_results = [
            BloodTestResult(
                id=beanie.PydanticObjectId(),
                **BloodTestSchema(
                    **results, kind=result_kind, test_at=blood_test_date
                ).model_dump(),
            )
            for result_kind, results in raw_blood_test_results["Sonuçlar"].items()
        ]
        await BloodTestResult.insert_many(default_user.blood_test_results)
        await default_user.replace(link_rule=WriteRules.WRITE)


class Backward:
    @free_fall_migration(document_models=[User, BloodTestResult])
    async def blood_test_result_revert_migration(self, session):
        default_user = await User.find(
            {User.email: "furkanmelihercan.98@gmail.com"}
        ).first_or_none()
        if default_user is None:
            return

        default_user.blood_test_results = []
        await default_user.replace(link_rule=WriteRules.WRITE)

        raw_blood_test_results = read_and_retrieve_static_results()
        blood_test_date = datetime.datetime.strptime(
            raw_blood_test_results["Tarih"], "%d.%m.%Y"
        )
        for result_kind in raw_blood_test_results["Sonuçlar"].keys():
            await BloodTestResult.find(
                {
                    BloodTestResult.kind: result_kind,
                    BloodTestResult.test_at: blood_test_date,
                }
            ).delete()
