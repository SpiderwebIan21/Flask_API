from resources.user import UserRegister
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenicate, identity
from resources.item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenicate, identity) #creates a new endpoint /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5500, debug=True)

