from flask import Flask, request
from flask_restful import Resource, Api

# no need to use jsonify with flask_restful
# as it automatically takes care of jsonification

app = Flask(__name__)

api = Api(app)

# list of items
items = []


class Item(Resource):
    def get(self, item_name):
        for item in items:
            if item['item_name'] == item_name:
                return item
        return {'item': None}, 404

    def post(self):
        data = request.get_json()
        item = {'item_name': data['item_name'], 'price': data['price']}
        items.append(item)
        return item, 201


# new resource
class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item', '/item/<string:item_name>')
api.add_resource(ItemList, '/items')

app.run(port=8090, debug=True)