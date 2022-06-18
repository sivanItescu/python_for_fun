import json
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)

# #Data base initialization
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'recruiter_database',
#     'host': 'localhost',
#     'port': 27017
# }
#
# db = MongoEngine()
# db.init_app(app)
#
# class User(db.Document):
#     name = db.StringField()
#     email = db.StringField()

jobs = {}


class Jobs(Resource):
    def get(self):
        return jobs

class Job(Resource):
    def get(self, job_id):
        return {job_id: jobs[job_id]}

    def post(self,job_id):
        jobs[job_id] = request.form['job_title']
        return {job_id: jobs[job_id]}, 201


api.add_resource(Jobs, '/alljobs')
api.add_resource(Job, '/jobs/<string:job_id>')

@app.route('/about')
def index():
    return jsonify({'name': 'irit',
                    'email': 'find_a_job@hotmail.com'})


if __name__ == '__main__':
    app.run(debug=True)

