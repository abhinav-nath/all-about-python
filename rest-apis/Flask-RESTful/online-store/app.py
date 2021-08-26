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
        item = next(filter(lambda x: x['item_name'] == item_name, items), None)

        # -- Same as below --
        # for item in items:
        #     if item['item_name'] == item_name:
        #         return item

        # -- In Java --
        # Item item = items.stream().filter(item -> item.getItemName() == itemName).findFirst();

        return {'item': item}, 200 if item else 404
        # same as below
        # return {'item': item}, 200 if item is not None else 404

    def post(self):
        data = request.get_json()

        if next(filter(lambda x: x['item_name'] == data['item_name'], items), None) is not None:
            return {'message': "An item with name '{}' already exists".format(data['item_name'])}, 400

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