from flask import request, jsonify
from . import create_app
from . import services
from config import products_collection
from controllers import get_products, add_product

app = create_app()


@app.route("/products", methods=["GET"])
def get_Allproducts():
    products = get_products
    if products:
        return jsonify(products=products)
    else:
        return jsonify("No Products in Database")


@app.route("/products", methods=["POST"])
def add_OneProduct():
    product = request.get_json()
    if product:
        add_product(product)
        return jsonify(
            message=f"Product '{product['ProductName']}' added successfully!"
        )
    else:
        return jsonify(
            message="Unable to Add Product", reason="No Products Data Provided"
        )
