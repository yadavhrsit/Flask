from config import orders_collection, cart_collection


def getOrders():
    orders = list(orders_collection.find({}, {"_id": 0}))
    return orders


def addOrder():
    orderList = list(cart_collection.find({}))
    if orderList:
        for item in orderList:
            orders_collection.insert_one(item)
        cart_collection.delete_many({})
        return orderList
