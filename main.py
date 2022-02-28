from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.job import Jobs
from forms.user import RegisterForm, LoginForm
from forms.jobs import JobForm
import datetime
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def works_log():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('works_log.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form, message="Такой пользователь уже есть")

        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_required
@app.route('/add_job',  methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        print(form.is_finished.data)
        job = Jobs(
            job=form.title.data,
            team_leader=form.team_leader_id.data,
            work_size=form.duration.data,
            collaborators=form.list_of_collaboration.data,
            is_finished=form.is_finished.data
        )
        current_user.jobs.append(job)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Add a Job', form=form)




def main():
    # db_name = input()
    db_name = "db/blogs.sqlite"
    db_session.global_init(db_name)
    app.run()

    db_sess = db_session.create_session()

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

    names = list()
    for user in db_sess.query(User).filter(User.address == 'module_1', User.age >= 21):
        print(user)
        user.address = 'module_3'
    db_sess.commit()

if __name__ == '__main__':
    main()