from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

Mongo_URL= os.getenv("MONGO_URL")
client = MongoClient(Mongo_URL)
db = client["retail_database"]
sales_data=db["sales_data"]