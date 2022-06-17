import json
from flask import Flask, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'recruiter_database',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()


@app.route('/')
def index():
    print("Hello world should be here")
    return jsonify({'name': 'irit',
                    'email': 'find_a_job@hotmail.com'})


if __name__ == '__main__':
    app.run(debug=True)

