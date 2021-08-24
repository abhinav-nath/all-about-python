from flask import Flask, jsonify, request


app = Flask(__name__)

# list of dictionaries
stores = [
    {
        'store_name': 'Toy Store',
        'items': [
            {
                'item_name': 'Rock Crawler',
                'price': 50.45
            },
            {
                'item_name': 'Ironman Action Figure',
                'price': 30.25
            }
        ]
    }
]


# POST /store  {store_name:x}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:store_name>')
def get_store(store_name):
    # iterate over stores
    # if the store name matches, return it
    # otherwise, return an error message
    for store in stores:
        if store['store_name'] == store_name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:store_name>/item', methods=['POST'])
def create_item_in_store(store_name):
    for store in stores:
        if store['store_name'] == store_name:
            request_data = request.get_json()
            new_item = {
                'item_name': request_data['item_name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:store_name>/item')
def get_items_from_store(store_name):
    for store in stores:
        if store['store_name'] == store_name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:store_name>/item/<string:item_name>', methods=['DELETE'])
def delete_item_from_store(store_name, item_name):
    for store in stores:
        if store['store_name'] == store_name:
            for item in store['items']:
                if item['item_name'] == item_name:
                    store['items'].remove(item)
                    return item_name + ' deleted successfully'
                return item_name + ' not found'
    return jsonify({'message': 'store not found'})


app.run(port=8090)
