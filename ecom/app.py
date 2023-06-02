from flask import Flask, jsonify, request
import json
from pymongo import MongoClient


client = MongoClient()
client = MongoClient(
    "mongodb+srv://harshityadav:JxsV3y4V7mWl8g1I@cluster0.s9trpdc.mongodb.net/"
)

db = client["Ecommerce"]
products_collection = db["products"]
orders_collection = db["order"]
cart_collection = db["cart"]


app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message="Welcome to the e-commerce application!")


# Products APIs
@app.route("/products", methods=["GET"])
def get_products():
    products = list(products_collection.find({}, {"_id": 0}))
    if products:
        return jsonify(products=products)
    else:
        return jsonify("No Products in Database")


@app.route("/products", methods=["POST"])
def add_product():
    product = request.get_json()
    if product:
        products_collection.insert_one(product)
        return jsonify(
            message=f"Product '{product['ProductName']}' added successfully!"
        )
    else:
        return jsonify(
            message="Unable to Add Product", reason="No Products Data Provided"
        )


# Cart APIs
@app.route("/cart", methods=["GET"])
def get_cart():
    cart = list(cart_collection.find({}, {"_id": 0}))
    if cart:
        total = 0
        for item in cart:
            total += int(item["Price"])
    else:
        return jsonify(message="Your Cart is Empty")
    return jsonify(Cart_Items=cart, Cart_Total_Value=total)


@app.route("/cart", methods=["POST"])
def add_cart():
    item = request.get_json()
    if products_collection.find_one(item):
        cart_collection.insert_one(item)
        return jsonify(
            message=f"Product '{item['ProductName']}' added to Cart successfully!"
        )
    else:
        return jsonify(message=f"Product '{item['ProductName']}' is unavailable!")


@app.route("/clearcart", methods=["GET"])
def clear_cart():
    cart_collection.delete_many({})
    return jsonify(message="All items have been Removed from the Cart")


# Orders APIs
@app.route("/orders", methods=["GET"])
def get_orders():
    orders = list(orders_collection.find({}, {"_id": 0}))
    if orders:
        return jsonify(Orders=orders)
    else:
        return jsonify(message="You Have'nt placed any orders yet")


@app.route("/orders", methods=["POST"])
def add_order():
    orderList = list(cart_collection.find({}))
    if orderList:
        for item in orderList:
            orders_collection.insert_one(item)
        cart_collection.delete_many({})
        return jsonify(
            message=f"Order Successful for the following Items : '{orderList}'"
        )
    else:
        return jsonify(message="No Items are available in the cart")


app.run()
