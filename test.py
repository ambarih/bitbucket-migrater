from flask import Flask
from flask_restplus import Api, Resource, fields
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app, version='1.0', title='MongoDB API', description='API for MongoDB data')

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['Jfrog-Nexus']
collection = db['bb']

# Define a namespace for MongoDB operations
ns = api.namespace('jfrog', description='JFrog operations')

# Function to create a route dynamically and store information in route_info dictionary
def create_route(endpoint, methods, description):
   
    dynamic_model = api.model(f'DynamicModel_{endpoint}', {
        'method': fields.String(required=True, description='HTTP method'),
        'endpoint': fields.String(required=True, description='API endpoint'),
        'description': fields.String(required=True, description=description),
    })

    @ns.route(f'/jfrog/{endpoint}')
    @ns.doc(params={'endpoint': 'API endpoint', 'description': 'Description of the endpoint'}, description=description)
    class DataResource(Resource):
        if 'GET' in methods:
            @api.marshal_with(dynamic_model)
            def get(self, endpoint):
                """ """
                data = collection.find_one({'endpoint': endpoint})
                if data:
                    return data
                else:
                    api.abort(404, f"Document with endpoint {endpoint} not found")

        if 'PUT' in methods:
            @api.marshal_with(dynamic_model)
            def put(self, endpoint):
                """ """
                return {'message': f'Updated document with endpoint {endpoint}'}

        if 'POST' in methods:
            @api.marshal_with(dynamic_model)
            def post(self, endpoint):
                """ """
                return {'message': 'New document created'}

        if 'DELETE' in methods:
            def delete(self, endpoint):
                """ """
                return {'message': f'Deleted document with endpoint {endpoint}'}

    return DataResource

# Create routes dynamically for each document in the collection
for document in collection.find():
    endpoint = document.get('endpoint', '')
    methods = document.get('method', '').split()
    description = document.get('description', '')
    route_class = create_route(endpoint, methods, description)
    ns.add_resource(route_class, f'/jfrog/{endpoint}')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
