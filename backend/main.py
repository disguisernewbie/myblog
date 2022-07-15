from typing import Mapping
from app import create_app
import requests
from flask_restful import Resource, Api

app = create_app('develop')


api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
print(app.url_map)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
