import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class Jobs (SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'
    # id team_leader job work_size collaborators is_finished
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)
    user = orm.relation('User')

    def __repr__(self):
        return f'<Job>{self.job}'