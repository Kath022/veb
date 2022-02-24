from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def works_log():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('works_log.html', jobs=jobs)


def main():
    # db_name = input()
    db_name = "db/blogs.sqlite"
    db_session.global_init(db_name)
    app.run()

    # db_sess = db_session.create_session()

    # user = User()
    # user.surname = 'Scott'
    # user.name = "Ridley"
    # user.age = 21
    # user.position = 'captain'
    # user.speciality = 'research engineer'
    # user.address = 'module_1'
    # user.email = "scott_chief@mars.org"
    # db_sess.add(user)
    #
    # for i in range(3):
    #     user = User()
    #     user.surname = f'колонист {i}'
    #     user.name = f'{i}'
    #     user.age = 20
    #     user.position = f'колонист {i}'
    #     user.speciality = f'колонист {i}'
    #     user.address = 'module_1'
    #     user.email = f"scott_chief{str(i) * 3}@mars.org"
    #     db_sess.add(user)
    #
    # job = Jobs()
    # job.team_leader = 1
    # job.job = 'deployment of residential modules 1 and 2'
    # job.work_size = 15
    # job.collaborators = '2, 3'
    # job.start_date = datetime.datetime.now()
    # job.is_finished = False
    # db_sess.add(job)
    #
    # db_sess.commit()

    # for user in db_sess.query(User).filter(User.address == 'module_1',
    #                                        User.speciality.notlike('engineer'),
    #                                        User.position.notlike('engineer')):
    #     print(user.id)



if __name__ == '__main__':
    main()