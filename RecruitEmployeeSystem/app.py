import json
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
import mongoengine as me
from marshmallow_mongoengine import ModelSchema
import datetime

app = Flask(__name__)
api = Api(app)

# Data base initialization
app.config['MONGODB_SETTINGS'] = {
    'db': 'recruiter_database',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)
me.connect('recruiter_database')

class CV(db.Document):
    id = db.IntField(primary_key=True, default=1)
    name = db.StringField()

cv1 = CV(id =368, name='Sivan Itescu').save()

class Job(me.Document):
    id = me.IntField(primary_key=True, default=1)
    title = me.StringField()
    description = me.StringField()
    location = me.StringField()
    is_open = me.BooleanField()
    last_time_opened = me.DateTimeField(default=datetime.datetime.utcnow)


class JobSchema(ModelSchema):
    class Meta:
        model = Job


job_schema = JobSchema()


class JobsResource(Resource):
    @classmethod
    def get(cls):
        jobs = []
        for loaded_job in Job.objects:
            jobs.append(job_schema.dump(loaded_job))
        return jobs


class JobResource(Resource):
    # def get(self, job_id):
    #     return {job_id: jobs[job_id]}

    @classmethod
    def put(cls,job_id):
        Job(id=job_id, title=request.form['job_title']).save()
        return {job_id: request.form['job_title']}, 201


api.add_resource(JobsResource, '/alljobs')
api.add_resource(JobResource, '/jobs/<string:job_id>')

@app.route('/about')
def index():
    return jsonify({'name': 'irit',
                    'email': 'find_a_job@hotmail.com'})


if __name__ == '__main__':
    app.run(debug=True)

