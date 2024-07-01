from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection, AsyncIOMotorDatabase
from app.Config import settings

class BaseRepository:
    def __init__(self, db_name: str, collection_name: str, uri: str = settings.MONGO_URL):
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = AsyncIOMotorClient(uri)
        self.db: AsyncIOMotorDatabase = self.client.get_database(db_name)
        self.collection: AsyncIOMotorCollection = self.db.get_collection(collection_name)

    
