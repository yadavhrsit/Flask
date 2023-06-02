from config import products_collection


def get_products():
    products = list(products_collection.find({}, {"_id": 0}))
    return products


def add_product(product):
    products_collection.insert_one(product)
