from flask import Flask, request, render_template
from flask_restful import Resource, Api
from Crypto.PublicKey import RSA

# creating the flask app
Asymmetric_Key_Gen = Flask(__name__)

# creating an API object
api = Api(Asymmetric_Key_Gen)

class KeyApp(Resource):
    def get(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        key = {'private_key':private_key, 'public_key':public_key}
        return render_template('index.html', key=key)

# adding the defined resources along with their corresponding urls
api.add_resource(KeyApp, '/key')

# driver function
if __name__ == '__main__':
    Asymmetric_Key_Gen.run(debug=True, host='127.0.0.1', port=8080)
