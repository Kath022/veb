import flask
from flask import request, jsonify
from . import db_session
from .job import Jobs

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    'id', 'team_leader', 'job',
                    'work_size', 'collaborators',
                    'start_date', 'end_date', 'is_finished'))
                    for item in jobs]
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job',
                  'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    exist_job = db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first()
    if exist_job is not None:
        return jsonify({'error': 'Id already exists'})

    job = Jobs(
        id=request.json['id'],
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'job': job.to_dict(only=(
                    'id', 'team_leader', 'job',
                    'work_size', 'collaborators',
                    'start_date', 'end_date', 'is_finished'))
        }
    )