from loguru import logger
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.user import User
from ..models.blood_test import BloodTestResult


async def initialize_mongo() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    print(client.db_name)
    await init_beanie(database=client.db_name, document_models=[User, BloodTestResult])
    logger.info("Beanie initialized.")
    return client
