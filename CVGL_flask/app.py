from flask import Flask, jsonify, request
import requests

URL = "https://fakestoreapi.com/products"
products = requests.get(URL).json()

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(product)

def get_element(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = max_id() + 1
    data['id'] = product_id
    products.append(data)
    return jsonify(data), 201

def max_id():
    if not products:
        return 0
    return max(product['id'] for product in products)

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    data = request.get_json()
    for id in data:
        product[id] = data[id]
    return jsonify(product)

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    products.remove(product)
    return jsonify({"message": "Producto eliminado exitosamente"}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
