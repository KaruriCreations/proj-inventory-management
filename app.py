from flask import Flask, jsonify, request

app = Flask(__name__)    

inventory = []

@app.route('/inventory', methods=['GET'])
def get_all_items():
    return jsonify({'inventory': inventory}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
