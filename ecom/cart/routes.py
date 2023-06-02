from flask import request, jsonify
from . import create_app
from . import services
from config import cart_collection, products_collection
from controllers import getCart, addItemToCart, emptyCart

app = create_app()


# Cart APIs
@app.route("/cart", methods=["GET"])
def get_cart():
    response = getCart()
    if response != 0:
        return jsonify(
            Cart_Items=response["Cart_Items"],
            Cart_Total_Value=response["Cart_Total_Value"],
        )
    else:
        return jsonify("There are no Items in Cart")


@app.route("/cart", methods=["POST"])
def add_cart():
    item = request.get_json()
    response = addItemToCart(item)

    if response:
        return jsonify(
            message=f"Product '{item['ProductName']}' added to Cart successfully!"
        )
    else:
        return jsonify(message=f"Product '{item['ProductName']}' is unavailable!")


@app.route("/clearcart", methods=["GET"])
def clear_cart():
    emptyCart()
    return jsonify(message="All items have been Removed from the Cart")
