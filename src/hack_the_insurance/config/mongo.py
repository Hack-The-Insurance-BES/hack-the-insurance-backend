from loguru import logger
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from ..models import User, BloodTestResult


async def initialize_mongo():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.db_name, document_models=[User, BloodTestResult])
    logger.info("Beanie initialized.")
