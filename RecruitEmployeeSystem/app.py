import json
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
import mongoengine as me
# from marshmallow_mongoengine import ModelSchema
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

class Job(db.Document):
    id = db.IntField(primary_key=True, default=1)
    title = db.StringField()
    # description = me.StringField()
    # location = me.StringField()
    # is_open = me.BooleanField()
    # last_time_opened = me.DateTimeField(default=datetime.datetime.utcnow)
    #
    # def __repr__(self):
    #     return '<Job(title = {self.title!r})>'.format(self=self)


# class JobSchema(ModelSchema):
#     class Meta:
#         model = Job


# job_schema = JobSchema()

# first_job = Job(id=123456,
#                 title='System analyzer',
                # description='System analyzer in a global company',
                # location='Tel-Aviv',
                # is_open=True).save()

first_job = Job(id=123456, title='System analyzer').save()
second_job = Job(id=123457, title='Python developer').save()
cv1 = CV(id =368, name='Sivan Itescu').save()
# print(first_job)
# dump_data = job_schema.dump(first_job).data
#
# job_schema.load(dump_data).data

# for job in Job.objects:
#     print(job.title)
# print(Job.objects)
# print(type(Job.objects))
# jobs = {}


class JobsResource(Resource):
    def get(self):
        result = {}
        for job in Job.objects:
            # print(j.title)
            result[job.id] = job.title
        return result

class JobResource(Resource):
    # def get(self, job_id):
    #     return {job_id: jobs[job_id]}

    def put(self,job_id):
        put_job = Job(id=job_id, title=request.form['job_title']).save()
        return {job_id: request.form['job_title']}, 201


api.add_resource(JobsResource, '/alljobs')
api.add_resource(JobResource, '/jobs/<string:job_id>')

@app.route('/about')
def index():
    return jsonify({'name': 'irit',
                    'email': 'find_a_job@hotmail.com'})


if __name__ == '__main__':
    app.run(debug=True)

