from flask import Flask, jsonify, request

app = Flask(__name__)


#Extraer productos de la API Fake
import requests
URL = "https://fakestoreapi.com/products"
products = requests.get(URL).json()

#Listado de productos
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

#Metodo de busqueda de productos
def get_element(product_id):
    isFound = False
    for product in products:
       if product["id"] == product_id:
            return product
    return None

#Metodo de extraer id maximo de productos
def max_id():
    maximo = products[0]['id']
    for product in products:
       if maximo < product['id'] :
          maximo = product['id']
    return maximo + 1

#Busqueda de producto
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_element(product_id)
    print(product)
    if product is None:
        return jsonify({"error": "Producto No encontrado"}), 404
    return jsonify(product)

#Agregar nuevo producto
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = max_id()
    data['id'] = product_id
    products.append(data)
    return jsonify(data), 201

#Eliminar producto producto
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto No encontrado"}), 404
    
    products = [product for product in products if product['id'] != product_id]
    return jsonify({"message": "Producto eliminado exitosamente"}), 200

# Modificar producto
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    
    # Validar datos de entrada
    if not all(key in data for key in ('title', 'price', 'description', 'category', 'image')):
        return jsonify({"error": "Faltan datos en la solicitud"}), 400
    
    product = get_element(product_id)
    if product is None:
        return jsonify({"error": "Producto No encontrado"}), 404
    
    # Actualizar producto
    for key, value in data.items():
        if key in product:
            product[key] = value
    
    return jsonify(product)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
