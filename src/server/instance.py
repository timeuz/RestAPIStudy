from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app, #objeto
            version='1.0',
            title='Simple book API',
            description='A simple book API',
            doc='/docs'
        )
    
    def run(self, ): #metodo para startar o server
        self.app.run(
            debug=True
        )
    
server = Server()