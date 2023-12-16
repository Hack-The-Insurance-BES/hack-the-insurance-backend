import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")

import json
import beanie
import datetime
from beanie import free_fall_migration

from src.hack_the_insurance.models.user import User
from src.hack_the_insurance.models.blood_test import BloodTestResult
from src.hack_the_insurance.schemas.blood_test import BloodTestSchema


class Forward:
    @free_fall_migration(document_models=[User])
    async def user_migration(self, session):
        exists = await User.find({User.email: "furkanmelihercan.98@gmail.com"}).exists()
        if exists is True:
            return

        default_user = User(
            id=beanie.PydanticObjectId(),
            name="Furkan Melih",
            family_name="Ercan",
            height=1.78,
            password="test",
            email="furkanmelihercan.98@gmail.com",
            birth_date=datetime.datetime(year=1998, day=30, month=8),
            blood_test_results=[],
        )
        await User.insert_one(default_user)


class Backward:
    @free_fall_migration(document_models=[User])
    async def user_revert_migration(self, session):
        await User.find({User.email: "furkanmelihercan.98@gmail.com"}).delete()
