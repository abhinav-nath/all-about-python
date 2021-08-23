from flask import Flask


app = Flask(__name__)

# list of dictionaries
stores = [
    {
        'name': 'Toy Store',
        'items': [
            {
                'name': 'Rock Crawler',
                'price': 50.45
            },
            {
                'name': 'Ironman Action Figure',
                'price': 30.25
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>')
def get_store():
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass


@app.route('/store/<string:name>/item')
def get_items_from_store():
    pass


app.run(port=8090)
