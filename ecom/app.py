from flask import Flask, jsonify, request
import json
from pymongo import MongoClient


client = MongoClient()
client = MongoClient('mongodb+srv://harshityadav:JxsV3y4V7mWl8g1I@cluster0.s9trpdc.mongodb.net/')
db = client['Ecommerce']
products_collection = db['products']
orders_collection = db['order']
cart_collection = db['cart']


app = Flask(__name__)

# products = [
#     {"pId": "1", "ProductName": "Noodles", "Price": "55", "Img_Url": "Noodles.png"},
#     {"pId": "2", "ProductName": "Burger", "Price": "60", "Img_Url": "Burger.png"},
#     {"pId": "3", "ProductName": "Pizza", "Price": "120", "Img_Url": "Pizza.png"},
#     {
#         "pId": "4",
#         "ProductName": "Cold Coffee",
#         "Price": "65",
#         "Img_Url": "Cold Coffee.png",
#     },
#     {"pId": "5", "ProductName": "Fries", "Price": "40", "Img_Url": "Fries.png"},
# ]

# cart = []
# orders = []


@app.route("/")
def index():
    return jsonify(message="Index")


# Products


@app.route("/products", methods=["GET"])
def get_products():
    result = list(products_collection.find({}))
    print(type(result))
    print(result)
    result = json.dumps(result)
    return result
    # return products_collection.find({},{'_id':0})
    # return jsonify(prodcuts=products_collection.find({},{'_id':0}))


@app.route("/products", methods=["POST"])
def add_product():
    product = request.get_json()
    products_collection.insert_one(product)
    return jsonify(message=f"Product '{product['ProductName']}' added successfully!")


# Cart
@app.route("/cart", methods=["GET"])
def get_cart():
    if len(cart) == 0:
        return jsonify(message="Empty Cart")
    else:
        total = 0
        for item in cart:
            total += int(item["Price"])
    return jsonify(Cart_Item=cart,Cart_Total_Value=total)


@app.route("/cart", methods=["POST"])
def add_cart():
    items=(request.get_json())
    totalItems = len(items)
    addedItems = 0
    if totalItems == 0:
        return jsonify(message="No Items to add in Cart")
    else:
        for item in items:
            pId = int(item["pId"])
            for product in products:
                if int(product["pId"]) == pId:
                    cart.append(product)
                    addedItems += 1
        if addedItems == 0:
            return jsonify(message="Order Failed: None of the Items are Available to Order")
        elif (addedItems!=totalItems):
            return jsonify(message=f"'{totalItems-addedItems}'Product Unavailable to Order")
        else:
            return jsonify(message=f"Order of items - '{items}' placed successfully!")


@app.route("/clearcart", methods=["GET"])
def clear_cart():
    cart.clear()
    return jsonify(message="All items have been Removed from the Cart")


# Order
@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders=orders)


@app.route("/orders", methods=["POST"])
def add_order():
    orderList = request.get_json()
    addedItems = 0
    totalItems = len(orderList)
    if len(orderList) == 0:
        return jsonify(message="Add an Item to Place an Order")
    if len(cart) == 0:
        return jsonify(message="Cart is Empty,add items in cart to place an order")
    for product in orderList:
        pId = int(product["pId"])
        for item in cart:
            if int(item["pId"]) == pId:
                orders.append(orderList)
                addedItems+=1              
    if addedItems == 0:
            return jsonify(message="Order Failed: None of the Items are in Cart")
    elif (addedItems!=totalItems):
            return jsonify(message=f"'{totalItems-addedItems}'Product not Found in Cart,Please add it to cart first")
    else:
        return jsonify(message=f"Order of items - '{orderList}' placed successfully!")

app.run()
