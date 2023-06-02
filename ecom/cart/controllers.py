from config import cart_collection
from flask import jsonify
from config import products_collection


def getCart():
    cart = list(cart_collection.find({}, {"_id": 0}))
    if cart:
        total = 0
        for item in cart:
            total += int(item["Price"])
    else:
        return 0
    return {"Cart_Items": cart, "Cart_Total_Value": total}


def addItemToCart(item):
    if products_collection.find_one(item):
        cart_collection.insert_one(item)
        return item


def emptyCart():
    cart_collection.delete_many({})
    return 1
