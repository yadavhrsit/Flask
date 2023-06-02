from flask import request, jsonify
from . import create_app
from . import services
from config import orders_collection, cart_collection
from controllers import getOrders, addOrder

app = create_app()


# Orders APIs
@app.route("/orders", methods=["GET"])
def get_orders():
    orders = getOrders()
    if orders:
        return jsonify(Orders=orders)
    else:
        return jsonify(message="You Have'nt placed any orders yet")


@app.route("/orders", methods=["POST"])
def add_order():
    orderList = addOrder()
    if orderList:
        return jsonify(
            message=f"Order Successful for the following Items : '{orderList}'"
        )
    else:
        return jsonify(message="No Items are available in the cart")
