from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Laptop', 'price': 800},
    {'id': 2, 'name': 'Smartphone', 'price': 500},
    {'id': 3, 'name': 'Tablet', 'price': 300},
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'message': 'Product not found'}), 404

@app.route('/products', methods=['POST'])
def create_product():
    new_product = {
        'id': len(products) + 1,
        'name': request.json['name'],
        'price': request.json['price']
    }
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        product['name'] = request.json.get('name', product['name'])
        product['price'] = request.json.get('price', product['price'])
        return jsonify(product)
    return jsonify({'message': 'Product not found'}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [prod for prod in products if prod['id'] != product_id]
    return jsonify({'message': 'Product deleted'})

if __name__ == '__main__':
    app.run(debug=True)

