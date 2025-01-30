import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
load_dotenv()

MONGOLAB_URI = os.getenv('MONGOLAB_URI')
# creating mongo client
client = MongoClient(MONGOLAB_URI, server_api = ServerApi('1'))

# sending a ping to test connection

try:
    client.admin.command('ping')
    print(' pinged to Mongodb . successfully connected ')
except Exception as e:
    print(e)