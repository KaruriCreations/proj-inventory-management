from flask import Flask, jsonify, request

app = Flask(__name__)    

inventory = []

@app.route('/inventory', methods=['GET'])
def get_all_items():
    return jsonify({'inventory': inventory}), 200

@app.route('/inventory/<int:id>', methods=['GET'])
def get_item(id):
    item = next((item for item in inventory if item['id'] == id), None)
    if item:
        return jsonify({'item': item}), 200
    return jsonify({'error': 'Item not found'}), 404

@app.route('/inventory', methods=['POST'])
def create_item():
    name = request.json['name']
    price = request.json['price']
    item = {'id': len(inventory) + 1, 'name': name, 'price': price}
    inventory.append(item)
    return jsonify({'item': item}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
