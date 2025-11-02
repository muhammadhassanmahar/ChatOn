from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_default_database()  # uses DB from URI or default
users_collection = db["users"]
messages_collection = db["messages"]
