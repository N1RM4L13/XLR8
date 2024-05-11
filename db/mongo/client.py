from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient


class BaseModel:

    def __init__(cls, client, database, collection):
        cls.__client = AsyncIOMotorClient(client)
        cls.__db = cls.__client[database]
        cls.__collection = cls.__client[database][collection]

    @classmethod
    async def create_collection(cls):
        pass


    @classmethod
    def get_collection(cls):
        # with open('../../../config.json') as handle:
        #     mongo_conn = json.loads(handle.read())
        # cls.__client = AsyncIOMotorClient(mongo_conn['conn_string'])
        return cls.__client[cls._db][cls.__collection]

    @classmethod
    async def insert_one(cls, document):
        result = await cls.get_collection().insert_one(document)
        return result.inserted_id

    @classmethods
    async def find_one(cls, document):
        result = await cls.get_collection().find_one(document)
        return result

    @classmethod
    async def find_all(cls, document):
        result = await cls.get_collection().find_all(document)
        return result

    @classmethod
    async def update_one(cls, old_document, new_document):
        result = await cls.get_collection().update_one(old_document, {'$set': new_document})
        return result

    @classmethod
    async def search_by_id(cls, id: str):
        result = await cls.get_collection().find_one({"_id": ObjectId(id)})
        return result

    @classmethod
    async def find(cls, document):
        cursor = cls.get_collection().find(document)
        result = await cursor.to_list()
        return result
