from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import sqlite3

class Account:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def write(self):
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()

        c.execute('''INSERT INTO accounts VALUES ('?', '?', '?')''',
                  self.username, self.password, self.email)
        # Create the table

        conn.commit()
        conn.close()

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email

    def __str__(self):
        return "Account('{}', '{}', '{}')".format(self.username, self.password, self.email)

    def safe_view(self):
        return {
            "username": self.username,
            "email": self.email
        }

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'hello': 'world'}

accounts = []

accountParser = reqparse.RequestParser()
accountParser.add_argument('username')
accountParser.add_argument('password')
accountParser.add_argument('email')

class Register(Resource):
    def post(self):
        args = accountParser.parse_args()
        username = args['username']
        password = args['password']
        email = args['email']

        new_account = Account(username, password, email)
        print(new_account)

        accounts.append(new_account)

api.add_resource(HelloWorld, '/')
api.add_resource(Register, '/register')

if __name__ == '__main__':
	app.run(debug=True)
