from pymongo import MongoClient
from bson import ObjectId
import config


def to_json(cart):
    return {
        "id": str(cart["_id"]),
        "Name": cart["Product_Name"],
        "Price": cart["Price"],
        "Img_Url": cart["Img_Url"],
        "pId": cart["pId"],
    }
