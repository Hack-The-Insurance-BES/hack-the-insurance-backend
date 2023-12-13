from beanie import free_fall_migration
from src.hack_the_insurance.models import User, BloodTestResult


class Forward:
    @free_fall_migration(document_models=[User, BloodTestResult])
    async def default_creations(self, session):
        pass


class Backward:
    @free_fall_migration(document_models=[User, BloodTestResult])
    async def revert_default_creations(self, session):
        pass
