from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


# Student class inherits Resource class
class Student(Resource):
    def get(self, name):
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')

app.run(port=8091)
