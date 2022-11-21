from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import pymongo
import certifi
ca = certifi.where()
import os



class MongoDBClient:
    client = None

    def __init__(self, database_name= DATABASE_NAME)-> None:
        try:
            if MongoDBClient.client is None:
                mongodb_url = os.getenv(MONGODB_URL_KEY)
                if 'localhost' in mongodb_url:
                    MongoDBClient.client= pymongo.MongoClient(mongodb_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongodb_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e     


