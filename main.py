from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    # app.run()

    user = User()
    user.surname = 'Scott'
    user.name = "Ridley"

    user.about = "биография пользователя 1"
    user.email = "email@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


    # new = False
    # db_sess = db_session.create_session()
    # if new:
    #     for i in range(3):
    #         user = User()
    #         user.name = f"Пользователь {i}"
    #         user.about = f"биография пользователя {i}"
    #         user.email = f"email{str(i) * 5}@email.ru"
    #         db_sess.add(user)
    # db_sess.commit()
    #
    # for user in db_sess.query(User).all():
    #     print(user.name)


if __name__ == '__main__':
    main()