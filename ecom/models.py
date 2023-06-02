from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb+srv://harshityadav:JxsV3y4V7mWl8g1I@cluster0.s9trpdc.mongodb.net/"
)
db = client["Ecommerce"]
