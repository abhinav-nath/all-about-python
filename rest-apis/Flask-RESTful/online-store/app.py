from flask import Flask
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

    def post(self, item_name):
        item = {'item_name': item_name, 'price': 12.00}
        items.append(item)
        return item, 201


api.add_resource(Item, '/item/<string:item_name>')

app.run(port=8090)