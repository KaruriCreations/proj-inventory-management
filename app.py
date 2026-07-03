from flask import Flask, jsonify, request
import requests

app = Flask(__name__)    

inventory = []

def fetch_inventory():
    try:
        #the api requires a header to work and authenticate us
        headers = {'User-Agent': 'InventoryApp/1.0'}
        # Search OpenFoodFacts specifically for food products
        url = 'https://world.openfoodfacts.org/cgi/search.pl?search_terms=food&search_simple=1&action=process&json=1&page_size=15'
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            products = response.json().get('products', [])
            for idx, prod in enumerate(products):
                name = prod.get('product_name') # Get the product name
                if name:
                    item = {
                        'id': len(inventory) + 1,
                        'name': name,
                        'price': 150 + (idx * 50) # Initiating KSH price since API doesn't have it
                    }
                    inventory.append(item)
    except Exception as e:
        print(f"API fetch failed: {e}")
        
#get our inventory
@app.route('/inventory', methods=['GET'])
def get_all_items():
    return jsonify({'inventory': inventory}), 200
#get a single item
@app.route('/inventory/<int:id>', methods=['GET'])
def get_item(id):
    item = next((item for item in inventory if item['id'] == id), None)
    if item:
        return jsonify({'item': item}), 200
    return jsonify({'error': 'Item not found'}), 404
#create a new item
@app.route('/inventory', methods=['POST'])
def create_item():
    name = request.json['name']
    price = request.json['price']
    item = {'id': len(inventory) + 1, 'name': name, 'price': price}
    inventory.append(item)
    return jsonify({'item': item}), 201
#update an item
@app.route('/inventory/<int:id>', methods=['PATCH'])
def update_item(id):
    item = next((item for item in inventory if item['id'] == id), None)
    if item:
        item['name'] = request.json['name']
        item['price'] = request.json['price']
        return jsonify({'item': item}), 200
    return jsonify({'error': 'Item not found'}), 404
#delete an item
@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = next((item for item in inventory if item['id'] == id), None)
    if item:
        inventory.remove(item)
        return jsonify({'message': 'Item deleted'}), 200
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    #calling our fetch_inventory function to get our inventory
    fetch_inventory()
    app.run(debug=True, port=5000)
