import motor.motor_asyncio

from src.config.settings import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MOTOR_DATABASE_URI)
db = client.food_fastapi


def get_collection(collection_name: str):
    return db.get_collection(collection_name)
