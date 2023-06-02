from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb+srv://harshityadav:JxsV3y4V7mWl8g1I@cluster0.s9trpdc.mongodb.net/"
)
db = client["Ecommerce"]


def to_json(orders):
    return {
        "id": str(orders["_id"]),
        "Name": orders["Product_Name"],
        "Price": orders["Price"],
        "Img_Url": orders["Img_Url"],
        "pId": orders["pId"],
    }
