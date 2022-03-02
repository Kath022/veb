import flask

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